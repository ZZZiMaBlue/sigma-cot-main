from tool import *
from llms import *
from tqdm import trange, tqdm
import re
import argparse
from prompts import *
from dotenv import load_dotenv
load_dotenv()


# ---------------- Argument Parsing ---------------- #
parser = argparse.ArgumentParser(description='SigMa CoT')
parser.add_argument('--dataset', type=str, required=True, help='dataset (e.g. msqa)')
parser.add_argument('--model', type=str, required=True, help='model (e.g. qwen_14b)')
parser.add_argument('--question_clarification_task', type=str, default='question_clarification')
parser.add_argument('--knowledge_evidence_task', type=str, default='knowledge_evidence')
parser.add_argument('--logic_task', type=str, default='logic')
parser.add_argument('--sentence_level_task', type=str, default='sentence_level')
parser.add_argument('--span_level_task', type=str, default='span_level')
args = parser.parse_args()

# ---------------- API Mapping ---------------- #
API_VERSION_MAP = {
    'gpt35': 'gpt35',
    'gpt4o': 'gpt4o',
    'dsv3': 'DeepSeekV3',
    'qwen': 'qwen',
    'llama': 'llama',
}
API_VERSION = API_VERSION_MAP.get(args.model.split('_')[0].lower(), 'gpt35')

# ---------------- Path Configuration ---------------- #
data_path = f"./dataset/{args.dataset}/test.json"
question_clarification_output_path = f"./result/1_1_Question_Clarification/{args.dataset}"
knowledge_evidence_output_path     = f"./result/1_2_Knowledge Evidence/{args.dataset}"
logic_output_path                  = f"./result/2_Logic/{args.dataset}"
sentence_level_output_path         = f"./result/3_1_Sentence_Level/{args.dataset}"
span_level_output_path             = f"./result/3_2_Span_Level/{args.dataset}"

question_clarification_output_file = f"{args.question_clarification_task}_{args.model}.json"
knowledge_evidence_output_file = f"{args.knowledge_evidence_task}_{args.model}.json"
logic_output_file = f"{args.logic_task}_{args.model}.json"
sentence_level_output_file = f"{args.sentence_level_task}_{args.model}.json"
span_level_output_file = f"{args.span_level_task}_{args.model}.json"


def set_openai_api(version=API_VERSION):
    if version in ["gpt35", "gpt4o"]:
        openai.api_base = os.getenv("OPENAI_API_BASE")
        openai.api_key = os.getenv("OPENAI_API_KEY")
    elif version == "DeepSeekV3":
        openai.api_base = os.getenv("DSV3_API_BASE")
        openai.api_key = os.getenv("DSV3_API_KEY")
    elif version == "qwen":
        openai.api_base = os.getenv("QWEN_API_BASE")
        openai.api_key = os.getenv("QWEN_API_KEY")
    else:
        raise ValueError("Unknown OpenAI API version")

set_openai_api()

def get_completion_for_api(version, prompt):
    if version == "gpt35":
        return get_completion_gpt35(prompt)
    elif version == "gpt4o":
        return get_completion_gpt4o(prompt)
    elif version == "DeepSeekV3":
        return get_completion_dsv3(prompt)
    elif version == "qwen":
        return get_completion_qwen(prompt)
    else:
        raise ValueError("Unknown API version")

# ---------------- Question Clarification ---------------- #
def process_question_clarification(data):
    for i in tqdm(range(len(data))):
        if "question_clar" in data[i] and data[i]["question_clar"]:
            continue
        context = data[i]["context"]
        question = data[i]["question"]
        prompt = question_clarification_prompt(context, question, args.dataset)
        try:
            response = get_completion_for_api(API_VERSION, prompt)
            match = re.search(r'(?:##?\s*Question Clarification:|Question Clarification:)\s*(.*)', response, re.DOTALL | re.IGNORECASE)
            data[i]["question_clar"] = match.group(1).strip() if match else "None"
            print(f"\nQuestion Clarification: {data[i]['question_clar']}")
        except Exception as e:
            print(f"Error in Question Clarification for item {i}: {e}")

# ---------------- Knowledge Evidence ---------------- #
def process_knowledge_evidence(data):
    for i in tqdm(range(len(data))):
        if "knowledge" in data[i] and data[i]["knowledge"] not in ([], [""], ["None"], ["N/A"], "", "None", "N/A"):
            continue
        if "knowledge" not in data[i] or data[i]["knowledge"] is None:
            data[i]["knowledge"] = ""
        context = data[i]["context"]
        question = data[i]["question"]
        question_clar = data[i]["question_clar"]
        prompt = knowledge_evidence_prompt(context, question, question_clar, args.dataset)
        try:
            response = get_completion_for_api(API_VERSION, prompt)
            print(response)
            know_match = re.search(r'(?:##?\s*Knowledge Evidences:|Knowledge Evidences:)\s*(.*)', response, re.DOTALL | re.IGNORECASE)
            know = know_match.group(1).strip() if know_match else "None"
            data[i]["knowledge"] = know
            print(f"\nKnowledge Evidences: {know}")
        except Exception as e:
            print(f"Error processing item {i}: {e}")

# ---------------- Logic ---------------- #
def process_logic(data):
    for i in tqdm(range(len(data))):
        if "answer_number" in data[i] and data[i]["answer_number"] not in ["", "0", "1", None]:
            continue
        context = data[i]["context"]
        question = data[i]["question"]
        question_clar = data[i].get("question_clar", "")
        knowledge = data[i].get("knowledge", "")
        prompt = logic_prompt(context, question, question_clar, knowledge, args.dataset)
        try:
            response = get_completion_for_api(API_VERSION, prompt)
            logic_match = re.search(r'(?:##?\s*Logical Steps:|Logical Steps:)\s*(.*?)\s*(?:##?\s*Answer\'s Number:|Answer\'s Number:|$)', response, re.DOTALL | re.IGNORECASE)
            number_match = re.search(r'(?:##?\s*Answer\'s Number:|Answer\'s Number:)\s*(\d+)', response, re.IGNORECASE)
            data[i]["logic"] = logic_match.group(1).strip() if logic_match else "None"
            data[i]["answer_number"] = number_match.group(1).strip() if number_match else "None"
            print(f"\nLogic: {data[i]['logic']}\nNumber: {data[i]['answer_number']}")
        except Exception as e:
            print(f"Error in Logic for item {i}: {e}")

# ---------------- Sentence Level ---------------- #
def process_sentence_level(data):
    for i in tqdm(range(len(data))):
        if "locate" in data[i] and data[i]["locate"] not in ([], [""], ["None"], ["N/A"], "", "None", "N/A"):
            continue
        if "locate" not in data[i] or data[i]["locate"] is None:
            data[i]["locate"] = ""
        context = data[i]["context"]
        question = data[i]["question"]
        knowledge = data[i].get("knowledge", "")
        logic = data[i].get("logic", "")
        number = data[i].get("answer_number", "")
        prompt = sentence_level_prompt(context, question, knowledge, logic, args.dataset)
        try:
            response = get_completion_for_api(API_VERSION, prompt)
            print(response)
            locate_match = re.search(r'(?:##?\s*Locate:|Locate)\s*(.*)', response, re.DOTALL | re.IGNORECASE)
            locate = locate_match.group(1).strip() if locate_match else "None"
            data[i]["locate"] = locate
            print(f"\nLocate: {locate}\n")
        except Exception as e:
            print(f"Error processing item {i}: {e}")

# ---------------- Span Level ---------------- #
def process_span_level(data):
    for i in tqdm(range(len(data))):
        if "answer_gpt" in data[i] and data[i]["answer_gpt"] not in ([""], ["None"], [], "", "None"):
            continue
        context = data[i].get("locate", "")
        question = data[i].get("question", "")
        number = data[i].get("answer_number", "")
        logic = data[i].get("logic", "")
        prompt = span_level_prompt(context, question, logic, number, args.dataset)
        try:
            response = get_completion_for_api(API_VERSION, prompt)
            print(f"\n{response}")
            answers_match = re.search(r'(?:##?\s*Answers:|Answers:)\s*(.*?)\s*(?:##?\s*Explanation:|Explanation:|$)', response, re.DOTALL | re.IGNORECASE)
            explanation_match = re.search(r'(?:##?\s*Explanation:|Explanation)\s*(.*)', response, re.DOTALL | re.IGNORECASE)
            answers_text = answers_match.group(1).strip() if answers_match else "None"
            explanation = explanation_match.group(1).strip() if explanation_match else "None"
            answers = [ans.strip() for ans in re.split(r'[;；\n]', answers_text) if ans.strip()]
            data[i]["answer_gpt"] = answers
            data[i]["explanation"] = explanation
            print(f"\nAnswers: {answers}\nExplanation: {explanation}")
        except Exception as e:
            print(f"Error processing item {i}: {e}")

# ---------------- Main Pipeline ---------------- #
def main():
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("\n=== Step 1: Question Clarification ===")
    process_question_clarification(data)
    save_dataset(question_clarification_output_path, question_clarification_output_file, data)
    print(f"Saved to: {os.path.join(question_clarification_output_path, question_clarification_output_file)}")

    print("\n=== Step 2: Knowledge Evidence ===")
    process_knowledge_evidence(data)
    save_dataset(knowledge_evidence_output_path, knowledge_evidence_output_file, data)
    print(f"Saved to: {os.path.join(knowledge_evidence_output_path, knowledge_evidence_output_file)}")

    print("\n=== Step 3: Logic ===")
    process_logic(data)
    save_dataset(logic_output_path, logic_output_file, data)
    print(f"Saved to: {os.path.join(logic_output_path, logic_output_file)}")

    print("\n=== Step 4: Sentence Level ===")
    process_sentence_level(data)
    save_dataset(sentence_level_output_path, sentence_level_output_file, data)
    print(f"Saved to: {os.path.join(sentence_level_output_path, sentence_level_output_file)}")

    print("\n=== Step 5: Span Level ===")
    process_span_level(data)
    save_dataset(span_level_output_path, span_level_output_file, data)
    print(f"Saved to: {os.path.join(span_level_output_path, span_level_output_file)}")


if __name__ == "__main__":
    main()
