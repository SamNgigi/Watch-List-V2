from . import db

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


class User(db.Model):
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
  username = db.Column(db.String(255))
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

  def __repr__(self):
    return f'User {self.username}'


class Role(db.Model):

  __tablename__ = 'roles'

  id = db.Column(db.Integer, primary_key = True)
  role_name = db.Column(db.String(255))
  """  
  The relationship defined here allows us to to reference a user role
  """
  users = db.relationship('User', backref = 'role', lazy = 'dynamic')

  def __repr__(self):
    return f'User {self.role_name}'

