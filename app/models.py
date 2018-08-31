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


  """  
  Every row must have a primary key set to it. By default the Column
  class has primary_key set to False. We want to set it to True on
  the id column to set it as the primary_key column.
  
  """
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  """ 
  We add a foreign key to the role class to reference a role.

  This role_id column is an interger column meant to reference the role id primary key related to a specific user.

  So for instance lets say we have a User "Daudi" and he is an Admin.

  We have the username defined in the User class and Admin role_name
  in the Role class.

  So say that Admin is of role id 1, if we wanted to know 

  Note here that the 'roles.id' is meant to reference the table name
  and locate the id.
  """
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

  """  
  The __repr__ function makes sure that our application refers to
  this class primarily by the username database-wise. So that it will
  be easier to identify database-errors associated with this class.
  """

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

  """  
  So let me see. 
    1. We have the role_id foreign key in the User class
    2. We have a db.relationship with a backref to the users in the
       Role class.
  
  So when we want to know the role of a particular User the backref
  to this one to many relationship allows us to use 'user.role.'

  So say now we want to know the user who belongs to a particular role, what could we do.

  Now when we use the accessor method Role.users it returns the user
  object. Now to access the username from the roles we loop through
  the role.users then with the single items call/find out the
  username. using role.username



  Lets take for example 3 roles. So multiple people can have only one
  user role and one user role and an role can have many users. As in,
  in an app many people can either be Premium, Basic or Admin users.

  role1 = Role(role_name = 'Admin')
  role2 = Role(role_name = 'Premium User')
  role2 = Role(role_name = 'Basic User')

  So say we have 3 users

  user1 = User(username = "IronMan", role_id = 1)
  user2 = User(username = "Thor", role_id = 2)
  user3 = User(username = "Thanos", role_id = 3)

  To get the role of a particular user we would only need to reference the backref and say

  user1.role = 'Admin'

  user3.role = 'Basic'

  What if we wanted to know the User belonging to a certian role. 

  One way;

  user_behind_this_role = Role.query.filter_by(id=1).first().

  We add the .first() because we want to return a real Object and not a Query Object. Applying .first() executes the query, instead of storing the Query object.

  Now a Real Object would return 
  
  <sqlalchemy.orm.dynamic.AppenderBaseQuery object at 0x7f3d5dab6eb8>

  A Query object returns

  <flask_sqlalchemy.BaseQuery object at 0x7f3d5d23d4a8>

  You definitely want to return a Real Object. It allows us to access
  the object's properties.

  From user_behind_this_role we would use the accessor "users"..loop
  through it to get to the username behind the role. So;

  for who_dat in user_behind_this_role.users:
    print(who_dat.username)

  This would return Admin.
  """