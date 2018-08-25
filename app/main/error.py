from flask import render_template
# from app import app replaced with
from . import main

@main.errorhandler(404)
def four_o_four(error):
  """  
  Function to render the 404 error page and the error status.
  """

  return render_template('404.html'),404