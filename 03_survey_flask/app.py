from flask import Flask, request, render_template
from surveys import satisfaction_survey

# Create the Flask app
app = Flask(__name__)

# Tracks user responses to a survey
responses = []
