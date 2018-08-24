"""  
Importing the render_template method that link view function to
templates.

We add the request object from flask and it encapsulates our HTTP
request with all its arguments to the view function.

We also import the redirect and url_for methods
"""
from flask import render_template, request, redirect, url_for
# Importing our app instance
from app import app
# Importing the get_movies function from request.py
from .request import get_movies, get_movie, search_movie

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

    # We fetch to movie_query from our search form
    movie_query = request.args.get('movie_query')

    # If we someone inputs a query
    if movie_query:
    # We redirect them to the search page via the search view function
        return redirect(url_for('search', movie_query=movie_query))
    else:
    # Else we continue displaying what we have now.
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

# We add a dynamic route that takes in a movie term
@app.route('/search/<movie_query>')
def search(movie_query):
    """ 
    View function to display the results of a search
    """
    query_term_list = movie_query.split(" ")
    formatted_query = "+".join(query_term_list)
    print(formatted_query)
    found_movies = search_movie(formatted_query)
    title = f'search results for {movie_query}'

    return render_template('search.html', found_movies=found_movies, title=title)

