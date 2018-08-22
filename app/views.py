"""  
Importing the render_template method that link view function to
template.
"""
from flask import render_template
# Importing our app instance
from app import app

# Our views


@app.route('/')
def index():
    """  
    View function that returns the index page and its data.
    """

    return render_template('index.html')
