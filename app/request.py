from app import app
import urllib.request, json
from .models import movie

Movie = movie.Movie

# Getting api key
api_key = app.config['MOVIE_DB_KEY']
# Getting the movie base url
base_url = app.config['MOVIE_DB_BASE_URL']


# Getting data from the Movie db api
def get_movies(category):
  """ 
  Function that gets the json response from our api call
  """
  get_movies_url = base_url.format(category, api_key)

  with urllib.request.urlopen(get_movies_url) as url:
    get_movies_data = url.read()
    get_movies_response = json.loads(get_movies_data)

    movie_results = None

    if get_movies_response['results']:
      movie_results_list = get_movies_response['results']
      # print(movie_results_list)
      movie_results = process_results(movie_results_list)

  return movie_results

def get_movie(id):
  get_movie_details_url = base_url.format(id, api_key)

  with urllib.request.urlopen(get_movie_details_url) as url:
    movie_details_data = url.read()
    movie_details_response = json.loads(movie_details_data)

    movie_object = None

    if movie_details_response:
      id = movie_detail_response.get('id')
      title = movie_detail_response.get('originalposter_title')
      overview = movie_detail_response.get('overview')
      poster = movie_detail_response.get('poster_path')
      vote_average = movie_detail_response.get('vote_average')
      vote_count = movie_detail_response.get('vote_count')
      
      movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object

# Process the response from the api call
def process_results(movie_list):
  movie_results = []
  for movie in movie_list:
    id = movie.get('id')
    title = movie.get('original_title')
    overview = movie.get('overview')
    poster = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    vote_count = movie.get('vote_count')

    if poster:
      movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
      movie_results.append(movie_object)

  return movie_results