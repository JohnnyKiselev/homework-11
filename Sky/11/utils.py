import json
from flask import render_template


def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        fin = file.read()
        fin = json.loads(fin)
    return fin


def show_candidate_page(candidate_id):
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if candidate_id == candidate['id']:
            return render_template('card.html', candidate=candidate)
    return 'Нет кандидата с таким ID.'


def search_by_name(name):
    candidates = load_candidates_from_json('candidates.json')
    candidates_filtred = []
    for candidate in candidates:
        if name.lower() in candidate['name'].lower():
            candidates_filtred.append(candidate)
    return candidates_filtred


def search_by_skill(skill):
    candidates = load_candidates_from_json('candidates.json')
    candidates_filtred = []
    for candidate in candidates:
        if skill.lower() in candidate['skills'].lower():
            candidates_filtred.append(candidate)
    return candidates_filtred


def show_page_index():
    candidates = load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)
