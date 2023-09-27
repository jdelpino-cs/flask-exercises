from flask import Flask, request, render_template, redirect
from surveys import satisfaction_survey

# Create the Flask app
app = Flask(__name__)

# Tracks user responses to a survey
responses = []


@app.route("/")
def home():
    """Show the home page."""
    return render_template("home.html",
                           survey=satisfaction_survey)


@app.route("/questions/<question_number>")
def question(question_number):
    """Show the first question."""
    return (
        render_template(
            'question.html',
            survey=satisfaction_survey,
            question_number=question_number)
    )


@app.route("/answer/", methods=["POST"])
def answer():
    """Add answer to responses and redirect to next question."""
    answer = request.form["answer"]
    responses.append(answer)
    return redirect(f"/questions/{len(responses)}")
