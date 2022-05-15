from typing import Optional

import flask 
from flask import Request
from wtforms import Form, BooleanField, PasswordField, validators

from viewmodels.shared.viewmodelbase import ViewModelBase

from infrastructure.cookie_auth import check_cookie_auth_username as get_username
# Add user service.


class CreateGameViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        
        self.player_one_username = get_username(self.request)
        self.error_p2 = None


    
       
