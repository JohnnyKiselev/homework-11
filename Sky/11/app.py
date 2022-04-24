import utils
from flask import Flask, render_template

app = Flask(__name__)

candidates = utils.load_candidates_from_json('candidates.json')


@app.route("/")
def page_index():
    result = 'Все кандидаты:'
    for candidate in candidates:
        result += f"<p><a href = '/candidate/{candidate['id']}'> {candidate['name']} </a></p>"
    return result


@app.route("/candidate/<int:x>")
def candidate_page(x):
    name = candidates[x-1]['name']
    position = candidates[x-1]['position']
    picture = candidates[x-1]['picture']
    skills = candidates[x-1]['skills']
    return render_template('card.html', name=name, position=position, picture=picture, skills=skills)


@app.route("/search/<x>")
def search_name(x):
    result = ''
    for candidate in candidates:
        if x in candidate['name'].lower():
            result += f"<p><a href = '/candidate/{candidate['id']}'> {candidate['name']} </a></p>"
    topic = f"""Найдено кандидатов: {result.count('a href')}"""
    summ = topic + result
    return summ


@app.route("/skill/<x>")
def search_skill(x):
    result = ''
    for candidate in candidates:
        if x in candidate['skills'].lower():
            result += f"<p><a href = '/candidate/{candidate['id']}'> {candidate['name']} </a></p>"
    topic = f"""Найдено кандидатов со скилом "{x}": {result.count('a href')}"""
    summ = topic + result
    return summ


app.run()
