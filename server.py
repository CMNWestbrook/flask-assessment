
from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "WhatWhatOhhYea"

# Makes it easier to debug if an undefined variable is in a Jinja template
# app.jinja_env.undefined = jinja2.StrictUndefined

@app.route('/')
def index():
    """Return the index.html page"""

    # return "Why did this work only once?"
    # return redirect('index.html')
    return render_template('index.html')

@app.route('/application-form')
def application_form():
    """Returns the application-form.html page"""

    return render_template('application-form.html')

@app.route('/application-success', methods=["POST"])
def application_response():
    """Returns the application response with information filled in"""
    first_name = request.form.get("firstname", "No first name?")
    last_name = request.form.get("lastname", "LAsttt")
    salary_requirement = request.form.get("salaryrequirement", "all the money")
    job = request.form.get('job', 'CEO')
    # job = request.args.get("job")

    if request.form['job'] == "softwareengineer":
        job = "Software Engineer" 

    elif request.form['job'] == "qaengineer":
        job = "QA Engineer"

    elif request.form['job'] == "productmanager":
        job = "Product Manager"


    return render_template('application-response.html',
                           firstname=first_name,
                           lastname=last_name,
                           salaryrequirement=salary_requirement,
                           job=job
                           )


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    # app.run(host="localhost")
    # app.run(host="127.0.0.1")
    app.run(host="0.0.0.0")
    # app.run(host="0.0.0.0", port=8000)
