from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField

class UserLoginForm (FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')