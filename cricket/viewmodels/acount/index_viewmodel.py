from typing import Optional

import flask 
from flask import Request
from cricket.viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        
        self.games = games_service_by_username(self.username)

