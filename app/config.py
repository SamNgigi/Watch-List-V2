class Config:
  """ 
  General parent configurations
  """
  pass

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

