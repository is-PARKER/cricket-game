from typing import Optional

import data.__db_session as db_session

from services.user_service import find_user_by_username
from data.games import Game
from data.innings import Inning


def get_games_count() -> int:
    session = db_session.create_session()
    try:
        return session.query(Game).count()
    finally:
        session.close()


def find_games_by_username(username: str) -> Optional[list[Game]]:
    session = db_session.create_session()
    try:
        return list(session.query(Game).filter(Game.player_one_username == username).order_by(Game.id.desc()))
    finally:
        session.close()


def create_game_with_inning(player_one_username: str, player_two_username: str) -> Optional[Game]:

    if not find_user_by_username(player_one_username):
        error = f"{player_one_username} was invalid"
        print(error)
        return None

    if not find_user_by_username(player_two_username):
        error = f"{player_two_username} was invalid"
        print(error)
        return None

    game = Game()
    game.player_one_username = player_one_username
    game.player_two_username = player_two_username

    session = db_session.create_session()

    inning = Inning()
    inning.player_one_username = player_one_username
    inning.player_two_username = player_two_username
    inning.game_id = game.id
    

    try:
        session.add(game)
        session.add(inning)
        session.commit()
    finally:
        session.close()

    return game


def find_game_by_id(game_id: int) -> Optional[Game]:
    session = db_session.create_session()
    try:
        game = session.query(Game).filter(Game.id == game_id).first()
        return game
    finally:
        session.close()