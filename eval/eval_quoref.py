"""
This evaluation script relies heavily on the one for DROP (``allennlp/tools/drop_eval.py``). We need a separate
script for Quoref only because the data formats are slightly different.
"""

import json
from typing import Dict, Tuple, List, Any, Optional
import numpy as np
from one_shot.eval_scripts.eval_script_drop import get_metrics


def _get_answers_from_data(annotations: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    If the annotations file is in the same format as the original data files, this method can be used to extract a
    dict of query ids and answers.
    """
    answers_dict: Dict[str, List[str]] = {}
    for article_info in annotations["data"]:
        for paragraph_info in article_info["paragraphs"]:
            for qa_pair in paragraph_info["qas"]:
                query_id = qa_pair["id"]
                candidate_answers = [answer["text"] for answer in qa_pair["answers"]]
                answers_dict[query_id] = candidate_answers
    return answers_dict


def evaluate_quoref(
    predicted_answers: Dict[str, Any], annotations: Dict[str, Any]
) -> Dict[str, float]:
    """
    Takes gold annotations and predicted answers and evaluates the predictions for each question
    in the gold annotations. Both JSON dictionaries must have query_id keys, which are used to
    match predictions to gold annotations.

    The ``predicted_answers`` JSON must be a dictionary keyed by query id, where the value is a
    list of strings (or just one string) that is the answer.
    The ``annotations`` are assumed to have either the format of the dev set in the Quoref data release, or the
    same format as the predicted answers file.
    """

    # Convert annotations if in the original data format
    if "data" in annotations:
        annotated_answers = _get_answers_from_data(annotations)
    else:
        annotated_answers = annotations

    instance_exact_match = []
    instance_f1 = []

    for query_id, candidate_answers in annotated_answers.items():
        max_em_score = 0.0
        max_f1_score = 0.0
        if query_id in predicted_answers:
            predicted = predicted_answers[query_id]
            gold_answer = tuple(candidate_answers)
            em_score, f1_score = get_metrics(predicted, gold_answer)
            if gold_answer[0].strip() != "":
                max_em_score = max(max_em_score, em_score)
                max_f1_score = max(max_f1_score, f1_score)
        else:
            print(f"Missing prediction for question: {query_id}")
            max_em_score = 0.0
            max_f1_score = 0.0
        instance_exact_match.append(max_em_score)
        instance_f1.append(max_f1_score)

    global_em = np.mean(instance_exact_match)
    global_f1 = np.mean(instance_f1)

    res = {
        'em': round(global_em * 100, 2),
        'f1': round(global_f1 * 100, 2)
    }
    return res


def read_predictions(pred_path: str) -> Dict[str, List[str]]:
    """
    Reads predictions in the new format and converts them to a dictionary keyed by query id.
    """
    dataset = json.load(open(pred_path, encoding="utf-8"))
    predictions = {item["id"]: item["answer_gpt"] for item in dataset}
    # predictions = {item["id"]: item["pred_answers"] for item in dataset}
    return predictions


def read_dataset(path: str):
    if path.endswith('jsonl'):
        dataset = []
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                dataset.append(json.loads(line))
    else:
        with open(path, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
    return dataset


gold_path = "/home/zhaoying/pycharm/one_shot/Quoref/dataset/origin.json"



if __name__ == "__main__":
    pred_path = "/home/zhaoying/pycharm/FBPrompt-main/results/quoref/qwen/bm25_correct_incorrect_miss_case3/prediction.json"

    # Read files
    predicted_answers = read_predictions(pred_path)
    gold_answers = json.load(open(gold_path, encoding="utf-8"))

    if "data" in gold_answers:
        gold_answers = _get_answers_from_data(gold_answers)

    # Evaluate
    result = evaluate_quoref(predicted_answers, gold_answers)
    print(result)
