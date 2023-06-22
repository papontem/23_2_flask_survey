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

# PAM: outmost storage of users RESPONSES as they travers through rpute ioon their way to complete survey
RESPONSES = []
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
    Shows a form with the current question, listing choices as radio options, and a text field if a text field is allowed.
    Form's action is a post request to route /answer with the users answer.
    PAM: DONE

    TODO: Step 6: Protecting Questions
    Right now, your survey app might be buggy. Once people know the URL structure, it's possible for them to manually go to /questions/3 before they've answered questions 1 and 2. They could also try to go to a question id that doesn't exist, like /questions/7.

    To fix this problem, you can modify your view function for the question show page to look at the number in the URL and make sure it's correct. If not, you should redirect the user to the correct URL.

    For example, if the user has answered one survey question, but then tries to manually enter /questions/4 in the URL bar, you should redirect them to /questions/1.

    Once they've answered all of the questions, trying to access any of the question pages should redirect them to the thank you page.

    """
    # storing the question in a variable for ease of call for later in the template.
    question = selected_survey.questions[question_id]

    return render_template('question.html', question=question, question_id = question_id,selected_survey=selected_survey)


@app.route('/answer', methods =["POST", "GET"])
def handle_question_answer():
    """TODO: Step 4
    Appends users answer to our fake DB object RESPONSES
    then send the user through a redirect to the next question.
    PAM: DONE so far
    """
    # get the answer from the form data, if text answer was given add it as a tuple to answer element thatll be added to responses with their answer choice.
    # print(request.args["answer"])

    # PAM: didnt work
    # if request.form.get("text_answer"):
    #     answer = (request.form.get("answer"), request.form["text_answer"])
    # else:
        # answer = request.form.get("answer")

    # PAM: attempt #5
    # if request.args["text_answer"]:
    #     answer = (request.args["answer"], request.args["text_answer"])
    # else:
        # answer = request.args["answer"]
    
    # PAM: attempt #7
    answer = request.args.get("answer")
    # append answer to the fake DB
    RESPONSES.append(answer)
    
    # move to the next question, assuming the user desnt stop and resubmit their question somehow X.X
    next_question_index = len(RESPONSES)
    """ 
    TODO: Step 5: 
    When survey is complete there wont be a next question so index will be out of range. directing user to a end of survey page.

    PAM: doing ... 
    """
    if next_question_index < len(selected_survey.questions):
        return redirect(f"/questions/{next_question_index}")
    else:
        return render_template("thank_you.html", responses=RESPONSES)

