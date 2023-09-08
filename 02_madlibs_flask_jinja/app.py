# Import Flask class from flask module
from flask import Flask, request, render_template

# Import a basic story from stories.py
from stories import story

# Instantiate a Flask object and store it in a variable called app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", prompts=story.prompts)


@app.route("/story", methods=["POST"])
def story_route():
    return render_template("story.html", story=story.generate(request.form))
