from typing import Optional

import flask 
from flask import Request

from cricket.infrastructure.to_int import to_int
from cricket.viewmodels.shared.viewmodelbase import ViewModelBase

# Add user service.


class PlayGameViewmodel(ViewModelBase):
    def __init__(self,game_id: int):
        super().__init__()
        self.game_id = game_id
        self.game = None

        if game_id:
            self.game = game_service.get_game_by_id(self.game_id)

        

        if self.game.latest_inning:
            self.inning = game_service.get_inning_by_latest(self.game_id)

    def validate():
        if not self.game:
            self.error = "Game is invalid."
    
        if self.game.player_one_username != self.username:
            self.error = "Players not logged in!"
