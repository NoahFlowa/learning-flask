from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	"""docstring for SignupForm"""
	first_name = StringField('First name', validators = [DataRequired("Please enter your First name")])
	last_name = StringField('Last name', validators = [DataRequired("Please enter your Last name")])
	email = StringField('Email', validators = [DataRequired("Please enter your Email"), Email("Please enter your Email")])
	password = PasswordField('Password', validators = [DataRequired("Please enter a Password"), Length(min = 6, message = "Your password must be 6 characters or more")])
	submit = SubmitField('Sign Up')

