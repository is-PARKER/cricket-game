from typing import Optional

import flask 
from flask import Request
from viewmodels.shared.viewmodelbase import ViewModelBase
from services.game_service import find_games_by_username

class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        
        self.games = find_games_by_username(self.username)

        

