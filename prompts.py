from example_data import example_msqa

def question_clarification_prompt(context, question, dataset):
    if dataset in ["msqa", "quoref", "quoref_m"]:
        example_keys = ["example_1", "example_2", "example_6"]
    elif dataset == "drop":
        example_keys = ["example_1", "example_7", "example_9"]
    elif dataset == "drop_m":
        example_keys = ["example_1", "example_7", "example_10"]
    else:
        raise ValueError(f"Unsupported dataset: {dataset}")

    prompt = f"""
    You need to analyze the question and identify the information needs based on the provided context. When answering, make sure to directly understand the question's intent without any unnecessary elaboration or deviation.

    1. A cognitive cue is a key insight that highlights the main information needed to answer the question. Generate up to three main phrases that summarize the key information needs, and separate them with semicolons.
    2. Identify the **central inquiry** of the question (i.e., what is the question specifically asking for?).
    3. Break down the core concepts and **key details** the question is focusing on (e.g., date, location, person, event, etc.).
    4. Define the **goal** of the question (i.e., what specific information or facts does the question aim to retrieve?).

    Please use the following format:
    ##Question Clarification: {{question clarification}}

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
        ##Question Clarification: {example['example_clar_msqa']}
        """

    prompt += f"""
    Now, based on the provided context, please analyze the question and extract the relevant information needs:
    Context: {context}
    Question: {question}
    """
    return prompt

def knowledge_evidence_prompt(context, question, question_clar, dataset):
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


def logic_prompt(context, question, question_clar, knowledge, dataset):
    if dataset in ["msqa", "quoref", "quoref_m"]:
        example_keys = ["example_1", "example_2", "example_6"]
    elif dataset == "drop":
        example_keys = ["example_1", "example_7", "example_9"]
    elif dataset == "drop_m":
        example_keys = ["example_1", "example_7", "example_10"]
    else:
        raise ValueError(f"Unsupported dataset: {dataset}")

    prompt = f"""
    Your task is to determine the number of distinct answers to the given question based on the provided context, question clarification, and knowledge evidences.

    Instructions:
    1. Assume that the question has multiple distinct answers.
    2. Identify all possible answers in the context, treating conjunctions like "and" or lists separated by commas as multiple distinct answers unless explicitly stated otherwise.
    3. If the question specifies a number of answers (e.g., "three"), provide that number as the answer's number.
    4. Carefully analyze the context, question clarification, and knowledge evidences to determine how many distinct answers are valid.

    After considering these steps, output the following:
    ##Logical Steps: {{Logical Steps}}
    ##Answer's Number: {{number}}

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
        Knowledge Evidences: {example['example_know_msqa']}
        ##Logical Steps: {example['example_logic_msqa']}
        ##Answer's Number: {example['example_number_msqa']}
        """

    prompt += f"""
    Now, give the answers to the following multi-answer questions along with the number of answers:
    Context: {context}
    Question: {question}
    Question Clarification: {question_clar}
    Knowledge Evidences: {knowledge}

    """
    return prompt

def sentence_level_prompt(context, question, knowledge, logic, dataset):
    if dataset in ["msqa", "quoref", "quoref_m"]:
        example_keys = ["example_1", "example_2", "example_6"]
    elif dataset == "drop":
        example_keys = ["example_1", "example_7", "example_9"]
    elif dataset == "drop_m":
        example_keys = ["example_1", "example_7", "example_10"]
    else:
        raise ValueError(f"Unsupported dataset: {dataset}")

    prompt = f"""
    Your task is to locate the sentences that contain the possible answers to the following question based on the provided question, context, and the information needs. When answering, make sure to directly understand the question's intent without any unnecessary elaboration or deviation.

    **Note**
    You **must** extract the exact original sentences from the context when locating the sentences. Do not modify or paraphrase the sentences in any way; they must be in their original form as they appear in the context.

    Please use the following format:
    ##Locate: 
    1. sentence1. # Must be the exact original sentence from the context.
    2. sentence2.
    3. sentence3.
    ...

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
        Knowledge Evidences: {example['example_know_msqa']}
        Logical Steps: {example['example_logic_msqa']}
        ##Locate:{example['example_locate_msqa']}
        """

    prompt += f"""
    Now, based on the information provided, please locate the sentences that contain the answers to the following question:
    Context: {context}
    Question: {question}
    Knowledge Evidences: {knowledge}
    Logical Steps: {logic}
    """
    return prompt

def span_level_prompt(locate, question, logic, number, dataset):
    if dataset in ["msqa", "quoref", "quoref_m"]:
        example_keys = ["example_1", "example_2", "example_6"]
    elif dataset == "drop":
        example_keys = ["example_1", "example_7", "example_9"]
    elif dataset == "drop_m":
        example_keys = ["example_1", "example_7", "example_10"]
    else:
        raise ValueError(f"Unsupported dataset: {dataset}")

    prompt = f"""
    Your task is to answer a question based on the provided context. The answer must be the exact words from the context (i.e., the original text). The answer may contain multiple items. Separate all answers with a semicolon. Keep answers as complete as possible. When answering, make sure to directly understand the question's intent without any unnecessary elaboration or deviation.
    If an answer includes terms with similar suffixes (e.g., "Moralistic political culture," "Individualistic political culture," and "Traditionalistic political culture"), remove the shared suffix ("political culture") and provide only the distinct parts ("Moralistic," "Individualistic," "Traditionalistic").
    If an answer includes text in parentheses (e.g., sphincter muscle (sphincter pupillae)), exclude the text inside the parentheses and only provide the main term.  

    "Answer's Number" represents the expected number of answers, but please note that this number is only for reference. 

    Please use the following format:
    ##Answers: {{answers1; answers2; answers3; ...}}
    ##Explanation: {{explanation}}  # Provide a clear and detailed explanation of how you reached the answers step by step.

    A few examples are as follows:
    """
    for i, example_key in enumerate(example_keys, 1):
        example = example_msqa.get(example_key)
        if not example:
            raise ValueError(f"Example key '{example_key}' not found in example_data.")
        prompt += f"""
        Example {i}:
        Context: {example['example_locate_msqa']}
        Question: {example['example_question_msqa']}
        Logical Steps: {example['example_logic_msqa']}
        Answer's Number: {example['example_number_msqa']}
        ##Answers:{example['example_answer_msqa']}
        ##Explanation:{example['example_explanation_msqa']}
        """

    prompt += f"""
    Now, use the format above to answer the following:
    Context: {locate}
    Question: {question}
    Logical Steps: {logic}
    Answer's Number: {number}

    """
    return prompt
