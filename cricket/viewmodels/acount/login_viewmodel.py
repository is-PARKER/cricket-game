from typing import Optional

import flask 
from flask import Request
from cricket.viewmodels.shared.viewmodelbase import ViewModelBase


class LoginViewmodel(ViewModelBase):
    def __init__(self):
        super().__init__()
        
        