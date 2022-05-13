from typing import Optional

import flask 
from flask import Request


from viewmodels.shared.viewmodelbase import ViewModelBase
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField



class LoginViewmodel(ViewModelBase):
    def __init__(self,form):
        super().__init__()
        self.username = self.request.form['username']
        self.password = self.request.form['password']


    def validate(self):

        if not self.username or not self.username.strip():
            self.error = 'Username is missing.'
        if not self.password:
            self.error = "Password is missing."

        