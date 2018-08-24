"""  
Importing the render_template method that link view function to
template.
"""
from flask import render_template
# Importing our app instance
from app import app
# Importing the get_movies function from request.py
from .request import get_movies, get_movie

# Our views


@app.route('/')
def index():
    """
    View function that returns the index page and its data.
    """
    title = 'Home | Watchlist'
    sup = 'Hello World!'
    popular_movies= get_movies('popular')
    upcoming_movies= get_movies('upcoming')
    now_playing= get_movies('now_playing')
    # print(popular_movies)
    return render_template('index.html', sup=sup, title=title, popular_movies=popular_movies, upcoming_movies=upcoming_movies, now_playing=now_playing)

# This is a dynamic url that takes in a specific id.
@app.route('/movie/<movie_id>')
def movie(movie_id):
    """  
    View function that returns the movie details page and its data.
    """
    title = f'Watchlist | M-{movie_id}'
    movie = get_movie(movie_id)
    return render_template('movie.html', movie_id=movie_id, title=title, movie=movie)

