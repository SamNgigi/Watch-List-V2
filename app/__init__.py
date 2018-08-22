from flask import Flask

# Initializing application. Creating our app instance.
app = Flask(__name__)

# This allows us to define our views on a separate file.
from app import views
