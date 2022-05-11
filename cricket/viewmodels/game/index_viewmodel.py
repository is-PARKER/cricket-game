from typing import Optional

import flask 
from flask import Request
from cricket.viewmodels.shared.viewmodelbase import ViewModelBase

from cricket.services.game_service import get_all_games_by_username
# Add user service.


class IndexViewmodel(ViewModelBase):
    def __init__(self):
        super().__init__()
        
        self.games = get_all_games_by_username(self.username)
