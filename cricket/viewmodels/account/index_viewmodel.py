from typing import Optional

import flask 
from flask import Request
from viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        
        from services.game_service import find_games_by_username
        self.games = find_games_by_username(self.username)
        



