import openai
import time

def log_error(e, attempt, retries, delay):
    print(f"{type(e).__name__}: {e}")
    if attempt < retries - 1:
        print(f"Retrying {attempt + 1}/{retries}, waiting {delay} seconds...")
    else:
        print("Maximum number of retries reached. Exiting.")


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
            print("KeyError: The key 'content' was not found in the response")
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
            print("KeyError: The key 'content' was not found in the response")
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
            print("KeyError: The key 'content' was not found in the response")
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
            print("KeyError: The key 'content' was not found in the response")
            return None
