from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# Importing our configurations dictionary.

# Instanciating LoginManager
login_manager = LoginManager()
"""  
The attribute below will monitor the changes in a user's request
header and log the user our.

We are able to set different levels of security.
"""
login_manager.session_protection = 'strong'
"""  
We prefix the login end point with the blueprint name because it is
located inside a blueprint.
"""
login_manager.login_view = 'auth.login'

# Instanciating the Bootstrap instance
bootstrap = Bootstrap()
# Instanciating our SQLAlchemy instance
db = SQLAlchemy()
  
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
  # Bootstrap(app)

  # Initializing our app as a SQLAlchemy instance.
  db.init_app(app)
  # Initializing LoginManager
  login_manager.init_app(app)

  # NOTE We will add the views and forms by adding our blueprint
  # Importing our blueprint
  from app.main import main as main_blueprint
  # Registering our blueprint
  app.register_blueprint(main_blueprint)
  # Importing our aut blueprint
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint, url_prefix='/auth')

  # Setting config
  from .request import configure_request
  configure_request(app)


  return app