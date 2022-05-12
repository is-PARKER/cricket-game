from ast import Pass
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField

class RegisterUserForm(Form):
    username = StringField('username', validators=[validators.Length(min=4, max=32)])
    email = StringField('email',validators=[validators.Length(min=6,max=120)])
    password = PasswordField('password',validators=[validators.DataRequired(),validators.EqualTo\
        ('confirm',message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')

class CreateGameForm(Form):
    player_two_username = StringField('player_two_username', validators=[validators.Length(min=4, max=32)])
    submit = SubmitField('Create')

class LoginForm(Form):
    username = StringField('username', validators=[validators.Length(min=4, max=32)])
    password = PasswordField('password')
    submit = SubmitField('Login')