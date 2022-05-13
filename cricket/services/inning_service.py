import imp
from typing import Optional
from data.games import Game
from data.innings import Inning

import data.__db_session as db_session


def get_innings_count() -> int:
    session = db_session.create_session()
    try:
        return session.query(Inning).count()
    finally:
        session.close()


def get_latest_innings() -> list[Inning]:
    session = db_session.create_session()
    try:
        return session.query(Inning).order_by(Inning.id.desc()).limit(5)
    finally:
        session.close()


def find_innings_by_game(game_id: str) -> Optional[list[Inning]]:
    session = db_session.create_session()
    try:
        return list(session.query(Inning).filter(Inning.game_id == game_id).order_by(Inning.game_id.desc()))
    finally:
        session.close()

def find_inning_by_game(game_id: str) -> Optional[Inning]:
    session = db_session.create_session()
    try:
        return session.query(Inning).filter(Inning.game_id == game_id).order_by(Inning.game_id.desc()).first()
    finally:
        session.close()


def create_new_inning(Inning: Inning) -> Optional[Inning]:
 

    inning = Inning()
    inning.inning = inning.inning + 1
    
    session = db_session.create_session()

    

    try:
        session.update(Game).where(Game.id == inning.game_id).values(inning = inning.inning)

        session.add(inning)
        
        session.commit()
    finally:
        session.close()

    return inning


def find_inning_by_id(inning_id: int) -> Optional[Inning]:
    session = db_session.create_session()
    try:
        inning = session.query(Inning).filter(Inning.id == inning_id).order_by(Inning.inning.desc()).first()
        return inning
    finally:
        session.close()