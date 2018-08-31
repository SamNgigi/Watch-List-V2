from flask import render_template
from . import auth


@auth.route('/login')
def login():
  test = 'Buyaaa'
  return render_template('auth/login.html', test=test)