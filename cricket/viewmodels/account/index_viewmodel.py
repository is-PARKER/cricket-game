from typing import Optional

import flask 
from flask import Request
from services.inning_service import find_inning_by_game, find_p1_score_by_id, find_p2_score_by_id
from viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        
        from services.game_service import find_games_by_username
       
        self.games = find_games_by_username(self.username)



        
        



