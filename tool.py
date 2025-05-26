import os
import json

def save_gold(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

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

def save_dataset(fold_path, file_name, prediction):
    os.makedirs(fold_path, exist_ok=True)
    with open(fold_path + '/' + file_name, 'w', encoding='utf-8') as f:
        json.dump(prediction, f, ensure_ascii=False, indent=2)
