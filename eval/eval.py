from copy import deepcopy
from tqdm import trange
from tool import read_dataset, save_dataset
# from eval_scripts.eval_script_clean import evaluate_msqa
from one_shot.eval_scripts.eval_script_msqa import evaluate_msqa

# 数据集路径
dataset_test = read_dataset(f'/home/zhaoying/pycharm/FBPrompt-main/results/quoref_m/qwen/bm25_correct_incorrect_miss_case3/prediction.json')

step_trange = trange(len(dataset_test))

preds, golds_revise, golds_original = {}, {}, {}
pred_count = 0
gold_revise_count = 0
gold_original_count = 0

for step in step_trange:
    sample = dataset_test[step]
    q_id = sample['id']

    if 'answers' in sample:
        golds_revise[q_id] = sample['answers']
        gold_revise_count += 1
    else:
        golds_revise[q_id] = ' '

for step in step_trange:
    # if sample['type'] != 'NUM':
    #     continue
    # if sample['type'] != 'DESC':
    #     continue
    # if sample['type'] not in ['HUM', 'LOC', 'ENTY']:
    #     continue
    sample = dataset_test[step]
    q_id = sample['id']

    if 'answer_gpt' in sample:
        preds[q_id] = sample['answer_gpt']
        pred_count += 1
    else:
        preds[q_id] = ' '

    if 'pred_answers' in sample:
        preds[q_id] = sample['pred_answers']
        pred_count += 1
    else:
        preds[q_id] = ' '

print("")
print(f"Number of samples with 'answer_gpt': {pred_count}")
print(f"Number of samples with 'answers' in 'test_revise.json': {gold_revise_count}")
print(f"Number of samples with 'answers' in 'test.json': {gold_original_count}")
print("")

# 确保preds和golds中没有空列表
for q_id, pred in preds.items():
    if isinstance(pred, list) and len(pred) == 0:
        print(f"Error: 'preds[{q_id}]' is an empty list")
        preds[q_id] = [""]

for q_id, gold in golds_revise.items():
    if isinstance(gold, list) and len(gold) == 0:
        print(f"Error: 'golds_revise[{q_id}]' is an empty list")
        golds_revise[q_id] = [""]

for q_id, gold in golds_original.items():
    if isinstance(gold, list) and len(gold) == 0:
        print(f"Error: 'golds_original[{q_id}]' is an empty list")
        golds_original[q_id] = [""]


try:
    result_scores_revise = evaluate_msqa(deepcopy(preds), deepcopy(golds_revise), brief=False)
    for key, value in result_scores_revise.items():
        print(f"'{key}': {value}")
except IndexError as e:
    print("An IndexError occurred during evaluation with 'test_revise.json'.")
    raise e