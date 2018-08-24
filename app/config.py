class Config:
  """ 
  General parent configurations
  """
  # We add the movie db base url
  """  
  This url is neat because it allows us to both pass a category to
  fetch multiple movies and an id to return just on movie.
  """
  MOVIE_DB_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
  MOVIE_DB_SEARCH_URL='https://api.themoviedb.org/3/search/movie?api_key={}&query={}'

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

