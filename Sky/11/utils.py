import json


def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        fin = file.read()
        fin = json.loads(fin)
    return fin


#print(load_candidates_from_json('candidates.json'))
