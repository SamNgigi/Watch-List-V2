from flask import Flask
from .config import DevConfig

# Initializing application. Creating our app instance.
app = Flask(__name__, instance_relative_config = True)

# Setting up our configurations. We pass in the DevConfig subclass.
app.config.from_object(DevConfig)
# We also add configuration to our config with api keys
app.config.from_pyfile('config.py')

# This allows us to define our views on a separate file.
from app import views
