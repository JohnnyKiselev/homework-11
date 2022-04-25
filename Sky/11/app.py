import utils
from flask import Flask

app = Flask(__name__)

candidates = utils.load_candidates_from_json('candidates.json')


@app.route("/")
def page_index():
    result = 'Все кандидаты:'
    for candidate in candidates:
        result += f"<p><a href = '/candidate/{candidate['id']}'> {candidate['name']} </a></p>"
    return result


@app.route("/candidate/<int:candidate_id>")
def candidate_page(candidate_id):
    return utils.show_candidate_page(candidate_id)


@app.route("/search/<name>")
def search_name(name):
    return utils.search_by_name(name)


@app.route("/skill/<skill>")
def search_skill(skill):
    return utils.search_by_skill(skill)


app.run()
