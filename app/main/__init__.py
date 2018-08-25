from flask import Blueprint

"""  
The Blueprint class takes in 2 arguments. 

Args:
  1. 'main' - The name of the blueprint.
  2. __name__ variable that points to the location of the blueprint.

  To avoid circular dependencies we import the views and errors
  modules
"""
main = Blueprint('main', __name__);

from . import views, error