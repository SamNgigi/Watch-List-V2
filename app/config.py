class Config:
  """ 
  General parent configurations
  """
  # We add the movie db base url
  MOVIE_DB_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'

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

