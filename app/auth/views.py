from . import auth
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db



@auth.route('/login', methods = ["GET", "POST"])
def login():
  login_form = LoginForm()
  if login_form.validate_on_submit():
    user = User.query.filter_by(email = login_form.email.data).first()
    if user is not None and user.verify_password(
      login_form.password.data
      ):
      """ 
      Below method take in the user object and the remember form data we then set a long
      time cookie in the browser as a result.
      """
      login_user(user, login_form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))
    
    flash("Invalid username or Password")

  title = "Watchlist Login"
  return render_template(
    'auth/login.html', title=title, login_form=login_form)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))
  

@auth.route("/register", methods = ["GET", "POST"])
def register():
  registration_form = RegistrationForm()
  if registration_form.validate_on_submit():
    user = User(
                email = registration_form.email.data,
                username = registration_form.username.data,
                password = registration_form.password.data
              )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("auth.login"))
    title = "New Account"

  return render_template(
    "auth/register.html", registration_form = registration_form)


  