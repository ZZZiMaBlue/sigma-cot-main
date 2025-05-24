import openai
import os
import time
import requests
from dotenv import load_dotenv, find_dotenv
import json
import random

def log_error(e, attempt, retries, delay):
    """
    打印错误信息和重试日志。
    """
    print(f"{type(e).__name__}: {e}")
    if attempt < retries - 1:
        print(f"重试 {attempt + 1}/{retries} 次，等待 {delay} 秒...")
    else:
        print("达到最大重试次数，退出。")


def get_completion_gpt35(prompt, temperature=0, model="gpt-3.5-turbo", retries=10, initial_delay=5, max_delay=30):

    messages = [{"role": "user", "content": prompt}]
    delay = initial_delay

    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message["content"]
        except (openai.error.ServiceUnavailableError,
                openai.error.PermissionError,
                openai.error.InvalidRequestError,
                openai.error.RateLimitError,
                openai.error.APIError,
                openai.error.Timeout) as e:

            log_error(e, attempt, retries, delay)

            if attempt < retries - 1:
                time.sleep(min(delay, max_delay))
                delay = min(delay * 2, max_delay)
            else:
                return None
        except KeyError:
            print("KeyError: 'content' 在响应中未找到")
            return None


def get_completion_gpt4o(prompt, temperature=0, model="gpt-4o-mini", retries=10, initial_delay=5, max_delay=30):

    messages = [{"role": "user", "content": prompt}]
    delay = initial_delay

    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message["content"]
        except (openai.error.ServiceUnavailableError,
                openai.error.PermissionError,
                openai.error.InvalidRequestError,
                openai.error.RateLimitError,
                openai.error.APIError,
                openai.error.Timeout) as e:

            log_error(e, attempt, retries, delay)

            if attempt < retries - 1:
                time.sleep(min(delay, max_delay))
                delay = min(delay * 2, max_delay)
            else:
                return None
        except KeyError:
            print("KeyError: 'content' 在响应中未找到")
            return None


def get_completion_dsv3(prompt, temperature=0, model="deepseek-chat", retries=10, initial_delay=5, max_delay=30):
    messages = [{"role": "user", "content": prompt}]
    delay = initial_delay

    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message["content"]
        except (openai.error.ServiceUnavailableError,
                openai.error.PermissionError,
                openai.error.InvalidRequestError,
                openai.error.RateLimitError,
                openai.error.APIError,
                openai.error.Timeout) as e:

            log_error(e, attempt, retries, delay)

            if attempt < retries - 1:
                time.sleep(min(delay, max_delay))
                delay = min(delay * 2, max_delay)
            else:
                return None
        except KeyError:
            print("KeyError: 'content' 在响应中未找到")
            return None


def get_completion_qwen(prompt, temperature=0, model="qwen2.5-14b-instruct", retries=10, initial_delay=5, max_delay=30):
    messages = [{"role": "user", "content": prompt}]
    delay = initial_delay

    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message["content"]
        except (openai.error.ServiceUnavailableError,
                openai.error.PermissionError,
                openai.error.InvalidRequestError,
                openai.error.RateLimitError,
                openai.error.APIError,
                openai.error.Timeout) as e:

            log_error(e, attempt, retries, delay)

            if attempt < retries - 1:
                time.sleep(min(delay, max_delay))
                delay = min(delay * 2, max_delay)
            else:
                return None
        except KeyError:
            print("KeyError: 'content' 在响应中未找到")
            return None


# DASHSCOPE_API_KEY = "sk-058a41b884bb4a26a0ddc6b56a2c2f72"
import requests
import time


def get_completion_llama(prompt, temperature=0, model="llama3-8b-instruct",
                         retries=10, initial_delay=5, max_delay=30):
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    # DASHSCOPE_API_KEY = "sk-058a41b884bb4a26a0ddc6b56a2c2f72" #182****2610
    # DASHSCOPE_API_KEY = "sk-3240372797a440b8b0599a7666e91daa" #177****3134
    DASHSCOPE_API_KEY = "sk-f5cebac76cf249a0a60a9036affe5712" #177****3134
    headers = {
        "Authorization": f"Bearer {DASHSCOPE_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "input": {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        },
        "parameters": {
            "result_format": "message",
            "temperature": temperature
        }
    }
    min_interval = 2
    last_request_time = 0
    delay = initial_delay
    for attempt in range(retries):
        try:
            elapsed = time.time() - last_request_time
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)

            last_request_time = time.time()

            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            result = response.json()
            return result["output"]["choices"][0]["message"]["content"]

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                elapsed = time.time() - last_request_time
                if elapsed < min_interval:
                    time.sleep(min_interval - elapsed)

                time.sleep(min(delay, max_delay))
                delay = min(delay * 2, max_delay)
            else:
                return None
        except KeyError:
            print("KeyError: 响应中未找到期望字段")
            return None



def get_completion_baidu(
        prompt,
        temperature=0,
        model="Qianfan-Chinese-Llama-2-7B-32K",  # 或其他支持的模型，如 "ERNIE-Bot-turbo"
        api_key="bce-v3/ALTAK-CKjXrZXAflyjdMvS9d6dU/c4f766bb1f2439d576f45b8ffb693d7e707d799b",  # 直接使用百度 API Key
        retries=3,
        initial_delay=5,
        max_delay=30,
        timeout=30,
):
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/{model}?access_token={api_key}"
    payload = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
    }
    headers = {'Content-Type': 'application/json'}

    delay = initial_delay
    for attempt in range(retries):
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(payload),
                timeout=timeout,
            )
            response.raise_for_status()  # 检查 HTTP 错误
            result = response.json()

            # 检查百度 API 是否返回错误
            if "error_code" in result:
                print(f"API Error: {result['error_msg']}")
                return None

            return result.get("result")  # 返回生成的文本

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(min(delay, max_delay))
                delay = min(delay * 2, max_delay)
            else:
                return None
        except KeyError:
            print("KeyError: 响应中未找到 'result' 字段")
            return None


def get_completion_dsr1(prompt, temperature=0, model="deepseek-reasoner", retries=10, initial_delay=5, max_delay=30):
    messages = [{"role": "user", "content": prompt}]
    delay = initial_delay

    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message["content"]
        except (openai.error.ServiceUnavailableError,
                openai.error.PermissionError,
                openai.error.InvalidRequestError,
                openai.error.RateLimitError,
                openai.error.APIError,
                openai.error.Timeout) as e:

            log_error(e, attempt, retries, delay)

            if attempt < retries - 1:
                time.sleep(min(delay, max_delay))
                delay = min(delay * 2, max_delay)
            else:
                return None
        except KeyError:
            print("KeyError: 'content' 在响应中未找到")
            return None


def get_completion_siliconflow(prompt, temperature=0, model="Pro/deepseek-ai/DeepSeek-V3", retries=10, initial_delay=5, max_delay=30):
    messages = [{"role": "user", "content": prompt}]
    delay = initial_delay

    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message["content"]
        except (openai.error.ServiceUnavailableError,
                openai.error.PermissionError,
                openai.error.InvalidRequestError,
                openai.error.RateLimitError,
                openai.error.APIError,
                openai.error.Timeout) as e:

            log_error(e, attempt, retries, delay)

            if attempt < retries - 1:
                time.sleep(min(delay, max_delay))
                delay = min(delay * 2, max_delay)
            else:
                return None
        except KeyError:
            print("KeyError: 'content' 在响应中未找到")
            return None


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
