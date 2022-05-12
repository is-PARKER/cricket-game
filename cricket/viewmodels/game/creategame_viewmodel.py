from typing import Optional
from xml.dom import ValidationErr

import flask 
from flask import Request
from wtforms import Form, BooleanField, Stringfield, PasswordField, validators

from cricket.viewmodels.shared.viewmodelbase import ViewModelBase

from infrastructure.cookie_auth import check_cookie_auth_username as get_username
# Add user service.


class CreateGameViewModel(ViewModelBase, form = None):
    def __init__(self):
        super().__init__()
        
        self.player_one_username = get_username(self.request)

        if form:
            player_two_username = form.username.data
            self.player_two_username = validate(player_two_username)

    def validate(self, username_check):
    
        if service.userservice.get_user_by_username(username_check):
            return username_check
        
        else:
            raise ValidationErr('Username not Created.')
