from typing import Optional

import flask 
from flask import Request
from cricket.viewmodels.shared.viewmodelbase import ViewModelBase

from cricket.services.user_service import get_user_count
from cricket.services.games_service import get_games_count
from cricket.services.innings_service import get_latest_innings

# Add user service.


class IndexViewModel():
    def __init__(self):
        super().__init__()
        
    self.innings = get_latest_innings()
    self.games_count = get_games_count()
    self.innings_count = get_games_count()
    self.user_count = get_user_count()