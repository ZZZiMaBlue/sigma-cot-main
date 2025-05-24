import openai
from tool import (save_dataset, get_completion_gpt35, get_completion_dsv3, get_completion_gpt4o, get_completion_siliconflow,
                  get_completion_qwen, get_completion_llama)
from example_data import example_msqa
import json
from tqdm import trange, tqdm
from msqa_en_utils import *
import time
import re
import random
import argparse

# 设置命令行参数
parser = argparse.ArgumentParser(description='Knowledge Evidence')
parser.add_argument('--dataset', type=str, required=True, help='dataset(e.g. msqa)')
parser.add_argument('--model', type=str, required=True, help='model(e.g. qwen_14b)')
parser.add_argument('--input_task', type=str, default='qc', help='input task: qc')
parser.add_argument('--output_task', type=str, default='ke', help='output task: ke')
args = parser.parse_args()

# 映射模型名称到API版本
API_VERSION_MAP = {
    'gpt3.5': 'gpt3.5',
    'gpt4o': 'gpt4o',
    'dsv3': 'DeepSeekV3',
    'siliconflow': 'SiliconFlow',
    'qwen': 'qwen',
    'llama': 'llama'
}

# 从完整模型名称中提取前缀(如qwen_14b -> qwen)
model_prefix = args.model.split('_')[0].lower()
API_VERSION = API_VERSION_MAP.get(model_prefix, 'gpt3.5')

# 设置文件路径
data_path = f"/home/zhaoying/pycharm/one_shot/result/1_1_Question_Clarification/{args.dataset}/{args.input_task}_{args.model}.json"
output_path = f"/home/zhaoying/pycharm/one_shot/result/1_2_Knowledge_Evidences/{args.dataset}"
output_file = f"{args.output_task}_{args.model}.json"

with open(data_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

def set_openai_api(version=API_VERSION):
    if version == "gpt3.5":
        openai.api_base = "https://xiaoai.plus/v1"
        openai.api_key = "sk-2e3on5zSxg6HvwUhl6kEypjai3iqDeSoTWakUt0iYUCwm487"
    elif version == "gpt4o":
        openai.api_base = "https://xiaoai.plus/v1"
        openai.api_key = "sk-W9iGrO1KhQb5mggbIIyewv26iZGGuygg10T8ccif2rbsdfN8"
    elif version == "DeepSeekV3":
        openai.api_base = "https://api.deepseek.com"
        openai.api_key = "sk-d344f57887e44357b482fc143b892dd3"
    elif version == "SiliconFlow":
        openai.api_base = "https://api.siliconflow.cn/v1"
        openai.api_key = "sk-yafxmrsdceofeztewjxckykrzxuacklegdfbcbvcxjiwnggx"
    elif version == "qwen":
        openai.api_base = "https://dashscope.aliyuncs.com/compatible-mode/v1"
        openai.api_key = "sk-058a41b884bb4a26a0ddc6b56a2c2f72"
    elif version == "llama":
        print("Using DashScope (LLaMA3) API — no need to set OpenAI API.")
    else:
        raise ValueError("Unknown API version specified.")

set_openai_api(version=API_VERSION)

def build_prompt(context, question, question_clar, dataset):
    if dataset in ["msqa", "quoref", "quoref_m"]:
        example_keys = ["example_1", "example_2", "example_6"]
    elif dataset == "drop":
        example_keys = ["example_1", "example_7", "example_9"]
    elif dataset == "drop_m":
        example_keys = ["example_1", "example_7", "example_10"]
    else:
        raise ValueError(f"Unsupported dataset: {dataset}")

    prompt = f"""
    Your task is to extract the key concepts from the provided context. Do not provide any explanation. When answering, make sure to directly understand the question's intent without any unnecessary elaboration or deviation.

    1. Extract the most critical pieces of information from the context that directly answer the question.
    2. Only provide the key concepts or facts that are highly relevant to the question (e.g., people, dates, events, etc.).
    3. Ensure each piece of information is clear and relevant to the question being asked.

    Please use the following format:
    ##Knowledge Evidences: {{knowledge evidences exploration}}

    A few examples are as follows:
    """
    for i, example_key in enumerate(example_keys, 1):
        example = example_msqa.get(example_key)
        if not example:
            raise ValueError(f"Example key '{example_key}' not found in example_data.")
        prompt += f"""
        Example {i}:
        Context: {example['example_context_msqa']}
        Question: {example['example_question_msqa']}
        Question Clarification: {example['example_clar_msqa']}
        ##Knowledge Evidences: {example['example_know_msqa']}
        """

    prompt += f"""
    Now, based on the provided context, please extract the relevant knowledge evidences:
    Context: {context}
    Question: {question}
    Question Clarification: {question_clar}

    """
    return prompt

def process_response(response, data, i):
    if response:
        know_match = re.search(r'(?:##?\s*Knowledge Evidences:|Knowledge Evidences:)\s*(.*)', response, re.DOTALL | re.IGNORECASE)
        know = know_match.group(1).strip() if know_match else "None"
        data[i]["knowledge"] = know
        print(f"\nKnowledge Evidences: {know}")

def process_data(data):
    for i in range(len(data)):
        if ("knowledge" in data[i] and data[i]["knowledge"] not in ([], [""], ["None"], ["N/A"])):
            continue

        if "knowledge" not in data[i] or data[i]["knowledge"] is None:
            data[i]["knowledge"] = ""

        context = data[i]["context"]
        question = data[i]["question"]
        question_clar = data[i]["question_clar"]

        prompt = build_prompt(context, question, question_clar, args.dataset)
        try:
            response = get_completion_for_api(API_VERSION, prompt)
            print(response)
            process_response(response, data, i)
        except Exception as e:
            print(f"Error processing item {i}: {e}")

def get_completion_for_api(version, prompt):
    if version == "gpt3.5":
        return get_completion_gpt35(prompt)
    elif version == "gpt4o":
        return get_completion_gpt4o(prompt)
    elif version == "DeepSeekV3":
        return get_completion_dsv3(prompt)
    elif version == "SiliconFlow":
        return get_completion_siliconflow(prompt)
    elif version == "qwen":
        return get_completion_qwen(prompt)
    elif version == "llama":
        return get_completion_llama(prompt)
    else:
        raise ValueError("Unknown API version specified.")


if __name__ == "__main__":
    start_time = time.time()
    total_item_time = 0

    for i in trange(len(data)):
        item_start = time.time()

        process_data([data[i]])
        save_dataset(output_path, output_file, data)
        with open(f"{output_path}/{output_file}", 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)

        item_end = time.time()
        total_item_time += (item_end - item_start)

    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_item_time / len(data) if len(data) > 0 else 0

    # 打印信息
    log_info = f"""
    ====== Running Statistics ======
    Total time   : {total_time:.2f} s
    Avg.time/data: {avg_time:.2f} s
    Data volume  : {len(data)} 
    API version  : {API_VERSION}
    Dataset name : {args.dataset}
    Model name   : {args.model}
    Input task   : {args.input_task}
    Output task  : {args.output_task}
    Input file   : {data_path}
    Output file  : {output_path}/{output_file}
    """

    print(log_info)

    # 保存到日志文件
    log_file = f"{output_path}/runlog_{args.dataset}_{args.model}_{args.output_task}.txt"
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_info + "\n")