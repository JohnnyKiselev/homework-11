import json
from flask import render_template


def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        fin = file.read()
        fin = json.loads(fin)
    return fin


candidates = load_candidates_from_json('candidates.json')


def show_candidate_page(candidate_id):
    name = candidates[candidate_id - 1]['name']
    position = candidates[candidate_id - 1]['position']
    picture = candidates[candidate_id - 1]['picture']
    skills = candidates[candidate_id - 1]['skills']
    return render_template('card.html', name=name, position=position, picture=picture, skills=skills)


def search_by_name(name):
    result = ''
    for candidate in candidates:
        if name in candidate['name'].lower():
            result += f"<p><a href = '/candidate/{candidate['id']}'> {candidate['name']} </a></p>"
    topic = f"""Найдено кандидатов: {result.count('a href')}"""
    summ = topic + result
    return summ


def search_by_skill(skill):
    result = ''
    for candidate in candidates:
        if skill in candidate['skills'].lower():
            result += f"<p><a href = '/candidate/{candidate['id']}'> {candidate['name']} </a></p>"
    topic = f"""Найдено кандидатов со скилом "{skill}": {result.count('a href')}"""
    summ = topic + result
    return summ
