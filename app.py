from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
debug = DebugToolbarExtension(app)


@app.route("/form")
def show_form():
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)


@app.route("/story")
def make_story():
    answers = request.args
    story_text = story.generate(answers)
    return render_template("story.html", text=story_text)
