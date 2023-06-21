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

@app.route('/') #decorator expecting a function
def homepage(): #the function that will be executed when decorator is flagged
    """Show homepage. PAM: render a page that shows the user the title of the survey, the instructions, and a button to start the survey."""
    
    # PAM: You have the avility to chose between two surveys
    # surveys = {"satisfaction": satisfaction_survey,"personality": personality_quiz}
    selected_survey = surveys["satisfaction"] #focusing on this one for now
    # selected_survey = surveys["personality"]

    # html = f"""
    # <html lang="en">
	# <head>
	# 	<meta charset="UTF-8" />
	# 	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		
	# 	<!--V-ANIMATED-Tab-Icon-V-->
	# 	<link rel="icon" type="gif" href="/static/pam_favicon_animated.gif" />

	# 	<title> Flask Survey Homepage </title>
	# </head>
    #     <body>
    #         <main>
    #             <header>
    #                 <h1>Home</h1>
    #                 <p>Welcome to this simple Flask Survey app</p>
    #             </header>
    #             <hr/>
    #             <h2>{selected_survey.title}</h2>
    #             <h3>Instructions</h3>
    #             <p>
    #                 {selected_survey.instructions}
    #             <p>
    #             <form action="/questions/0">
    #                 <button>Start!</button>
    #             </form>
    #             <hr/>
    #             <footer>
	# 			<section class="Footer_Content">
	# 				<p>&copy; Phedias A.M. All Rights Reserved</p>
	# 			</section>
	# 		</footer>
    #         </main>
    #     </body>
    # </html>
    # """
    # return html
    return render_template("startpage.html", selected_survey=selected_survey)