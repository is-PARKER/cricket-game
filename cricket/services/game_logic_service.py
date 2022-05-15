from typing import Optional

import data.__db_session as db_session

from services.user_service import find_user_by_username
from data.games import Game
from data.innings import Inning
from services import game_service