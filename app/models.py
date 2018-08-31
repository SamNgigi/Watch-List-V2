from werkzeug.security import (
  # Method that takes in a password hash and returns a hash of it
  generate_password_hash,
  # Method compares two hashes
  check_password_hash
)
"""  
UserMixin allows our user model to inherit the following methods

is_authenticated() - Returns a boolean if User is authenticated or na

is_active() - Check if a use is in an active session.

is_anonymous() - Returns boolean if User is anonymous.

get_id() - Returns a unique identifier for User
"""
from flask_login import UserMixin
from . import login_manager
from . import db

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class Movie:
  """  
  Movie class to define movie objects
  """

  def __init__(self, id, title, overview, poster, vote_average, vote_count):
    self.id = id
    self.title = title
    self.overview = overview
    self.poster = "https://image.tmdb.org/t/p/w500" + poster
    self.vote_average = vote_average
    self.vote_count = vote_count

class Review:

  all_reviews = []

  def __init__(self, movie_id, title, imageurl, review):
    self.movie_id = movie_id
    self.title = title
    self.imageurl = imageurl
    self.review = review

  def save_review(self):
    Review.all_reviews.append(self)

  @classmethod
  def get_reviews(cls, id):

    response = []

    for review in cls.all_reviews:
      if review.movie_id == id:
        response.append(review)

    return response

  @classmethod
  def clear_review(cls):
    Review.all_reviews.clear()


class User(UserMixin, db.Model):
  """  
  User class that defines and helps us create a new user.

  We pass in db.Model as an argument which will help our class connect to our database and allow communication.

  __tablename__ var allows us to name our database column.

  We create columns using the db.Column class which will represent a
  single column. We also pass in the datatype to be stored as the
  first argument.
  """
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255), index=True)
  email = db.Column(db.String(255), unique=True, index=True)
  # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  password_hash = db.Column(db.String(255))

  @property
  def password(self):
    """  
    We use the @decorator to create a write only class property
    password.

    Note that used on the password entered into a form in the views.

    We block access to the password property raising an Attribute
    error because it is not secure for Users to have access to that
    property.
    """
    raise AttributeError('You cannot read the password attribute')

  """  
  When we set this property (password) we generate a password hash and pass the hashed password as a value to the password_hash column property to save to the database.
  """
  @password.setter
  def password(self, password):
    self.password_hash = generate_password_hash(password)


  def verify_password(self, password):
    """  
    This function takes in our password hashes it then compares it to
    the hashed one we had stored in our database.
    """
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return f'User {self.username}'


class Role(db.Model):

  __tablename__ = 'roles'

  id = db.Column(db.Integer, primary_key = True)
  role_name = db.Column(db.String(255))
  """  
  The relationship defined here allows us to to reference a user role
  """
  # users = db.relationship('User', backref = 'role', lazy = 'dynamic')

  def __repr__(self):
    return f'User {self.role_name}'

