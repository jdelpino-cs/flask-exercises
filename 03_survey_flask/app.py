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
    question_number = int(question_number)
    if (question_number < len(satisfaction_survey.questions)
            and question_number == len(responses)):
        return (
            render_template(
                'question.html',
                survey=satisfaction_survey,
                question_number=question_number,
                question=satisfaction_survey.questions[question_number])
        )
    elif question_number >= len(satisfaction_survey.questions):
        return render_template('thank_you.html',
                               survey=satisfaction_survey)
    else:
        return render_template("error.html")


@app.route("/answer", methods=["POST"])
def answer():
    """Add answer to responses and redirect to next question."""
    answer = request.form["choice"]
    responses.append(answer)
    return redirect(f"/questions/{len(responses)}")
