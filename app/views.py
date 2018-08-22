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
    title = 'Home | Watchlist'
    sup = 'Hello World!'
    return render_template('index.html', sup=sup, title=title)

# This is a dynamic url that takes in a specific id.
@app.route('/user/<user_id>')
def movie(user_id):
    """  
    View function that returns the movie details page and its data.
    """
    return render_template('movie.html', user_id=user_id)

