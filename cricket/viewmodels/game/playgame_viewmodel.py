from typing import Optional

import flask 
from flask import Request

from viewmodels.shared.viewmodelbase import ViewModelBase

# Add user service.


class PlayGameViewmodel(ViewModelBase):
    def __init__(self,game_id: int):
        super().__init__()
        self.game_id = game_id
        self.game = None
        self.hit = None

        if game_id:
            from services import game_service
            self.game = game_service.find_game_by_id(self.game_id)
            if not self.game:
                return None
        
        else:
            self.error = "Game is not created"        

        if self.game:
            from services import inning_service
            self.inning = inning_service.find_inning_by_game(self.game_id)


