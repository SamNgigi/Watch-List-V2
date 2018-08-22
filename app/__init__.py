from flask import Flask
from .config import DevConfig

# Initializing application. Creating our app instance.
app = Flask(__name__)

# Setting up our configurations. We pass in the DevConfig subclass.
app.config.from_object(DevConfig)

# This allows us to define our views on a separate file.
from app import views
