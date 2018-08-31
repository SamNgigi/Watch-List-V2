"""  
Importing os allows our application to interact with the operating
system dependant functionality.
"""
import os

class Config:
  """ 
  General parent configurations

  The base url is neat because it allows us to both pass a category to
  fetch multiple movies and an id to return just on movie.
  """

  MOVIE_DB_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
  MOVIE_DB_SEARCH_URL='https://api.themoviedb.org/3/search/movie?api_key={}&query={}'

  # We add our movie api key
  MOVIE_DB_KEY = os.environ.get('MOVIE_DB_KEY')

  # We add the secret key
  SECRET_KEY = os.environ.get('SECRET_KEY')

  """  
  We add this line to remove the SQLAlchemy notifications every time
  we launch our app
  """
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  """  
  Adding our connection with Postgres data base via our SQLAlchemy ORM
  """
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:Sam@localhost/watchlist'


class ProdConfig(Config):
  """ 
  Production parent configurations

  Args:
    We inherit the general configurations from Config
  """
  pass

class DevConfig(Config):
  """ 
  Development parent configurations

  Args:
    We inherit the general configurations from Config  
  """
  DEBUG= True


"""  
Config option dictionary helps us access different configuration
option classes.
"""
config_options = {
  'development': DevConfig,
  'production': ProdConfig
}

