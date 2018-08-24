from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

# Initializing application. Creating our app instance.
app = Flask(__name__, instance_relative_config = True)

"""  
Configurations
"""
# Setting up our configurations. We pass in the DevConfig subclass.
app.config.from_object(DevConfig)
# We also add configuration to our config with api keys
app.config.from_pyfile('config.py')

"""  
Initializing flask extensions
"""
# Initializing Bootstrap in our app.
bootstrap = Bootstrap(app)

# This allows us to define our views on a separate file.
from app import views
