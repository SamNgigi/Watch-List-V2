from flask import Flask
from flask_bootstrap import Bootstrap
# Importing our configurations dictionary.
from config import config_options
# Instanciating the Bootstrap instance
bootstrap = Bootstrap()
  
def create_app(config_name):
  """  
  Function that instantiates our flask app and allows us to pass in a
  configuration option.

  It also initialize flask extensions on our application.
  """

  app = Flask(__name__)

  # Creating the app configurations
  # We replace app.config.from_pyfile("config.py") with this.
  app.config.from_object(config_options[config_name])

  """  
  Initializing flask extensions.
  We call the init_app() on an extension to complete their
  initialization.

  So we are basically kind of saying add bootstrap on app
  initialization.
  """
  bootstrap.init_app(app)

  # NOTE We will add the views and forms by adding our blueprint
  # Importing our blueprint
  from .main import main as main_blueprint
  # Registering our blueprint
  app.register_blueprint(main_blueprint)

  # Setting config
  from .request import configure_request
  configure_request(app)


  return app