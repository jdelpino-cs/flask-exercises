from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

# Create the Flask app
app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.config['SECRET_KEY'] = "chickenzarecoo121837"

# Initialize the debug toolbar and disable redirects
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route("/")
def home():
    """Show the home page."""
    return render_template("home.html",
                           survey=satisfaction_survey)


@app.route("/start")
def start():
    """Clear the session of responses."""
    session["responses"] = []
    session.modified = True
    return redirect("/questions/0")


@app.route("/questions/<question_number>")
def question(question_number):
    question_number = int(question_number)
    if (question_number < len(satisfaction_survey.questions)
            and question_number == len(session["responses"])):
        return (
            render_template(
                'question.html',
                survey=satisfaction_survey,
                question_number=question_number,
                question=satisfaction_survey.questions[question_number])
        )
    elif (question_number >= len(satisfaction_survey.questions)
          and question_number == len(session["responses"])):
        return render_template('thank_you.html',
                               survey=satisfaction_survey)
    else:
        flash(
            "You tried invalid question number…"
            "And we redirected you to the current question."
        )
        return redirect(f'/questions/{len(session["responses"])}')


@app.route("/answer", methods=["POST"])
def answer():
    """Add answer to responses and redirect to next question."""
    answer = request.form["choice"]
    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses
    return redirect(f'/questions/{len(session["responses"])}')
