#!/usr/bin/python

from collections import defaultdict
from typing import Any, Dict, List, Set, Tuple, Union, Optional
import json
import argparse
import string
import re

import numpy as np
from scipy.optimize import linear_sum_assignment


# From here through _normalize_answer was originally copied from:
# https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/
# Then cleaned up and modified a bit.
def _remove_articles(text: str) -> str:
    regex = re.compile(r"\b(a|an|the)\b", re.UNICODE)
    return re.sub(regex, " ", text)


def _white_space_fix(text: str) -> str:
    return " ".join(text.split())


EXCLUDE = set(string.punctuation)


def _remove_punc(text: str) -> str:
    if not _is_number(text):
        return "".join(ch for ch in text if ch not in EXCLUDE)
    else:
        return text

def _lower(text: str) -> str:
    return text.lower()


def _tokenize(text: str) -> List[str]:
    return re.split(" |-", text)


def _normalize_answer(text: str) -> str:
    """Lower text and remove punctuation, articles and extra whitespace."""

    parts = [
        _white_space_fix(_remove_articles(_normalize_number(_remove_punc(_lower(token)))))
        for token in _tokenize(text)
    ]
    parts = [part for part in parts if part.strip()]
    normalized = " ".join(parts).strip()
    return normalized


def _is_number(text: str) -> bool:
    try:
        float(text)
        return True
    except ValueError:
        return False


def _normalize_number(text: str) -> str:
    if _is_number(text):
        return str(float(text))
    else:
        return text


def _answer_to_bags(
    answer: Union[str, List[str], Tuple[str, ...]]
) -> Tuple[List[str], List[Set[str]]]:
    if isinstance(answer, (list, tuple)):
        raw_spans = answer
    else:
        raw_spans = [answer]
    normalized_spans: List[str] = []
    token_bags = []
    for raw_span in raw_spans:
        normalized_span = _normalize_answer(raw_span)
        normalized_spans.append(normalized_span)
        token_bags.append(set(normalized_span.split()))
    return normalized_spans, token_bags


def _align_bags(predicted: List[Set[str]], gold: List[Set[str]]) -> List[float]:
    """
    Takes gold and predicted answer sets and first finds the optimal 1-1 alignment
    between them and gets maximum metric values over all the answers.
    """
    scores = np.zeros([len(gold), len(predicted)])
    for gold_index, gold_item in enumerate(gold):
        for pred_index, pred_item in enumerate(predicted):
            if _match_numbers_if_present(gold_item, pred_item):
                scores[gold_index, pred_index] = _compute_f1(pred_item, gold_item)
    row_ind, col_ind = linear_sum_assignment(-scores)

    max_scores = np.zeros([max(len(gold), len(predicted))])
    for row, column in zip(row_ind, col_ind):
        max_scores[row] = max(max_scores[row], scores[row, column])
    return max_scores


def _compute_f1(predicted_bag: Set[str], gold_bag: Set[str]) -> float:
    intersection = len(gold_bag.intersection(predicted_bag))
    if not predicted_bag:
        precision = 1.0
    else:
        precision = intersection / float(len(predicted_bag))
    if not gold_bag:
        recall = 1.0
    else:
        recall = intersection / float(len(gold_bag))
    f1 = (
        (2 * precision * recall) / (precision + recall)
        if not (precision == 0.0 and recall == 0.0)
        else 0.0
    )
    return f1


def _match_numbers_if_present(gold_bag: Set[str], predicted_bag: Set[str]) -> bool:
    gold_numbers = set()
    predicted_numbers = set()
    for word in gold_bag:
        if _is_number(word):
            gold_numbers.add(word)
    for word in predicted_bag:
        if _is_number(word):
            predicted_numbers.add(word)
    if (not gold_numbers) or gold_numbers.intersection(predicted_numbers):
        return True
    return False


def get_metrics(
    predicted: Union[str, List[str], Tuple[str, ...]], gold: Union[str, List[str], Tuple[str, ...]]
) -> Tuple[float, float]:
    """
    Takes a predicted answer and a gold answer (that are both either a string or a list of
    strings), and returns exact match and the DROP F1 metric for the prediction.  If you are
    writing a script for evaluating objects in memory (say, the output of predictions during
    validation, or while training), this is the function you want to call, after using
    :func:`answer_json_to_strings` when reading the gold answer from the released data file.
    """
    predicted_bags = _answer_to_bags(predicted)
    gold_bags = _answer_to_bags(gold)

    if set(predicted_bags[0]) == set(gold_bags[0]) and len(predicted_bags[0]) == len(gold_bags[0]):
        exact_match = 1.0
    else:
        exact_match = 0.0

    f1_per_bag = _align_bags(predicted_bags[1], gold_bags[1])
    f1 = np.mean(f1_per_bag)
    f1 = round(f1, 2)
    return exact_match, f1


def answer_json_to_strings(answer: Dict[str, Any]) -> Tuple[Tuple[str, ...], str]:
    """
    Takes an answer JSON blob from the DROP data release and converts it into strings used for
    evaluation.
    """
    if "number" in answer and answer["number"]:
        return tuple([str(answer["number"])]), "number"
    elif "spans" in answer and answer["spans"]:
        return tuple(answer["spans"]), "span" if len(answer["spans"]) == 1 else "spans"
    elif "date" in answer:
        return (
            tuple(
                [
                    "{0} {1} {2}".format(
                        answer["date"]["day"], answer["date"]["month"], answer["date"]["year"]
                    )
                ]
            ),
            "date",
        )
    else:
        raise ValueError(
            f"Answer type not found, should be one of number, spans or date at: {json.dumps(answer)}"
        )



def evaluate_drop(
    predicted_answers: Dict[str, Any], annotations: Dict[str, Any]
):
    """
    Takes gold annotations and predicted answers and  evaluates the predictions for each question
    in the gold annotations.  Both JSON dictionaries must have query_id keys, which are used to
    match predictions to gold annotations (note that these are somewhat deep in the JSON for the
    gold annotations, but must be top-level keys in the predicted answers).

    The ``annotations`` are assumed to have the format of the dev set in the DROP data release.
    The ``predicted_answers`` JSON must be a dictionary keyed by query id, where the value is a string
    (or list of strings) that is the answer.
    """

    predicted_answers_dict = {item["id"]: item["answer_gpt"] for item in predicted_answers}
    # predicted_answers_dict = {item["id"]: item["pred_answers"] for item in predicted_answers}

    instance_exact_match = []
    instance_f1 = []
    # for each type as well
    for passage_id, data in annotations.items():
        qa_pairs = data["qa_pairs"]
        max_em_score = 0.0
        max_f1_score = 0.0

        for qa_pair in qa_pairs:
            query_id = qa_pair["query_id"]

            if query_id in predicted_answers_dict:
                predicted = predicted_answers_dict[query_id]
                # print(predicted)

                candidate_answers = [qa_pair.get("answer")]

                if "validated_answers" in qa_pair and qa_pair["validated_answers"]:
                    candidate_answers.extend(qa_pair["validated_answers"])
                for answer in candidate_answers:
                    gold_answer, gold_type = answer_json_to_strings(answer)
                    em_score, f1_score = get_metrics(predicted, gold_answer)
                    if gold_answer[0].strip() != "":
                        max_em_score = max(max_em_score, em_score)
                        max_f1_score = max(max_f1_score, f1_score)
            else:
                print(f"Error: No prediction found for query_id {query_id}")

        instance_exact_match.append(max_em_score)
        instance_f1.append(max_f1_score)

    global_em = np.mean(instance_exact_match)
    global_f1 = np.mean(instance_f1)
    result = {
        'exact': round(global_em*100, 2),
        'f1': round(global_f1 * 100, 2)
    }
    return result





if __name__ == "__main__":
    prediction_path = '/home/zhaoying/pycharm/one_shot/result/three-shot/drop_qwen_14b.json'

    gold_path = '/home/zhaoying/pycharm/one_shot/drop/dataset/drop_first_dataset_dev.json'
    annotations = json.load(open(gold_path, encoding="utf-8"))
    predicted_answers = json.load(open(prediction_path, encoding="utf-8"))
    result = evaluate_drop(predicted_answers, annotations)
    print(result)