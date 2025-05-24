import json
import warnings
def get_entities(label, token):
    prev_tag = 'O'
    begin_offset = 0
    chunks = []

    # check no ent
    if isinstance(label[0], list):
        for i, s in enumerate(label):
            if len(set(s)) == 1:
                chunks.append(('O', -i, -i))
    # for nested list
    if any(isinstance(s, list) for s in label):
        label = [item for sublist in label for item in sublist + ['O']]
    if any(isinstance(s, list) for s in token):
        token = [item for sublist in token for item in sublist + ['O']]

    for i, chunk in enumerate(label + ['O']):
        if chunk not in ["O", "B", "I"]:
            warnings.warn('{} seems not to be IOB tag.'.format(chunk))
        tag = chunk[0]
        if end_of_chunk(prev_tag, tag):
            chunks.append((' '.join(token[begin_offset:i]), begin_offset, i - 1))
        if start_of_chunk(prev_tag, tag):
            begin_offset = i
        prev_tag = tag
    return chunks


def end_of_chunk(prev_tag: str, tag: str):
    """Determine if we are at the end of an answer chunk.

    :param prev_tag: previous tag
    :param tag: current tag
    """
    chunk_end = False
    if prev_tag == 'B' and tag == 'B':
        chunk_end = True
    if prev_tag == 'B' and tag == 'O':
        chunk_end = True
    if prev_tag == 'I' and tag == 'B':
        chunk_end = True
    if prev_tag == 'I' and tag == 'O':
        chunk_end = True
    return chunk_end


def start_of_chunk(prev_tag: str, tag: str):
    """Determine if we are at the start of an answer chunk.

    :param prev_tag: previous tag
    :param tag: current tag
    """
    chunk_start = False
    if tag == 'B':
        chunk_start = True
    if prev_tag == 'O' and tag == 'I':
        chunk_start = True
    return chunk_start


def read_gold(gold_file):
    """Read the gold file

    :param gold_file: file path to the file with the golden answers
    """
    with open(gold_file,"r",encoding="utf-8") as f:
        data = json.load(f)['data']
        golds = {}
        for piece in data:
            golds[piece['id']] = {}
            golds[piece['id']] ["type"] = piece['type']
            golds[piece['id']]['question'] = " ".join(piece['question'])
            golds[piece['id']]['context'] = " ".join(piece['context'])
            golds[piece['id']]["answer"] = set(map(lambda x: x[0], get_entities(piece['label'], piece['context'])))
    return golds


if __name__ == '__main__':
    msqa_en_test = read_gold('msqa_en_test.json')

    example_ids = list(msqa_en_test.keys())
    for example_id in example_ids[:10]:
        print(msqa_en_test[example_id]['question'])
        print(msqa_en_test[example_id]['context'])
        print(msqa_en_test[example_id]['answer'])
        print("\n")