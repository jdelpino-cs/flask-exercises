# Import Flask class from flask module
from flask import Flask

# Instantiate a Flask object and store it in a variable called app
app = Flask(__name__)


@app.route("/welcome")
def welcome():
    return "welcome"


@app.route("/welcome/home")
def welcome_home():
    return "welcome home"


@app.route("/welcome/back")
def welcome_back():
    return "welcome back"
