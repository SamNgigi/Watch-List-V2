from flask_wtf import FlaskForm
from wtforms import (
  StringField, PasswordField, SubmitField, BooleanField
)
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
  email = StringField("Email Address", validators=[Required(),Email()])
  username = StringField("Username", validators=[Required()])
  password = PasswordField('Password', validators=[Required(),EqualTo("password_confirm",message = "Passwords must match")])
  password_confirm = PasswordField("Confirm Passwords",validators =[Required()])
  submit = SubmitField("Sign Up")

  """ Custom Validators """
  def validate_email(self, data_field):
    if User.query.filter_by(email = data_field.data).first():
      raise ValidationError("There is an account with that email")
      
  """ 
  Remember we use .first() in order to return real Objects not Query
  objects
  """
  def validate_username(self, data_field):
    if User.query.filter_by(username = data_field.data).first():
      raise ValidationError("Tha username is taken")


class LoginForm(FlaskForm):
  email = StringField("Email Address", validators = [Required(), Email()])
  password = PasswordField("Password", validators = [Required()])
  remember = BooleanField("Remember me")
  submit = SubmitField("Sign In")