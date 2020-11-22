# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flasklogin import models

class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField("Log in")

class RegistrationForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(),Email()])
  username = StringField('Username',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!')])
  pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
  submit = SubmitField('Register!')

  def validate_email(self,field):
    if models.User.query.filter_by(email=field.data).first():
      raise ValidationError('Email has been registered')

  def validate_username(self,field):
    if models.User.query.filter_by(username=field.data).first():
      raise ValidationError("Username is taken!")