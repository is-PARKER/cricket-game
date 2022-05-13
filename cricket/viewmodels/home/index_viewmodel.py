from typing import Optional

import flask 
from flask import Request
from viewmodels.shared.viewmodelbase import ViewModelBase



# Add user service.


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        
        from services.user_service import get_user_count
        from services.game_service import get_games_count
        from services.inning_service import get_latest_innings

        self.innings = get_latest_innings()
        self.games_count = get_games_count()
        self.innings_count = get_games_count()
        self.user_count = get_user_count()