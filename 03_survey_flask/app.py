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
    if (question_number == len(responses) + 1
            and question_number <= len(satisfaction_survey.questions)):
        return (
            render_template(
                'question.html',
                survey=satisfaction_survey,
                question_number=int(question_number),
                question=satisfaction_survey.questions[int(question_number)])
        )
    elif question_number > len(satisfaction_survey.questions):
        return render_template('results.html')


@app.route("/answer", methods=["POST"])
def answer():
    """Add answer to responses and redirect to next question."""
    answer = request.form["choice"]
    responses.append(answer)
    return redirect(f"/questions/{len(responses) + 1}")
