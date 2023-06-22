# save this as app.py
from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

#flask requiered app name
app = Flask(__name__)

#flask debugtoolbar settings
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app) 

# PAM: outmost storage of users responses as they travers through rpute ioon their way to complete survey
responses = []
# PAM: You have the avility to chose between two surveys. surveys = {"satisfaction": satisfaction_survey,"personality": personality_quiz}
selected_survey = surveys["satisfaction"] #focusing on this one for now
# selected_survey = surveys["personality"]

@app.route('/') #decorator expecting a function
def homepage(): #the function that will be executed when decorator is flagged
    """TODO: Step 2
    Show homepage. 
    PAM: render template for startpage that shows the user the title of the survey, the instructions, and a button to start the survey.
    """
    

    return render_template("startpage.html", selected_survey=selected_survey)


@app.route('/questions/<int:question_id>')
def show_desired_question(question_id):
    """TODO: Step 3
    renders questions template for any question from the selected survey.
    Shows a form with the current question, listing choices as radio options, TODO: add a text field if a text field is allowed.
    Form's action is a post request to route /answer with the users answer.
    """

    return render_template("question.html", question_id = question_id, selected_survey=selected_survey)

@app.route("/answer", methods=["POST"])
def get_question_answer():
    """ PAM TODO: WEll touch this in step 4"""

    html = f"{responses}"
    return html
