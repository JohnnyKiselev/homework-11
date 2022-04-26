import utils
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def page_index():
    return utils.show_page_index()


@app.route("/candidate/<int:candidate_id>")
def candidate_page(candidate_id):
    return utils.show_candidate_page(candidate_id)


@app.route("/search/<name>")
def search_name(name):
    candidates = utils.search_by_name(name)
    return render_template('search.html', candidates=candidates, len_candidates=len(candidates))


@app.route("/skill/<skill>")
def search_skill(skill):
    candidates = utils.search_by_skill(skill)
    return render_template('skill.html', candidates=candidates, len_candidates=len(candidates))


app.run()
