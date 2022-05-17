from sqlalchemy import bindparam, text,update
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

def update_inning_by_dart(inning_id: int, score: int, col_to_mark: str, mark_update: int) -> Optional[Inning]:
    session = db_session.create_session()

    try: 
        inning = session.query(Inning).filter(Inning.id == inning_id).order_by(Inning.inning.desc()).first()
        
        if inning.player_turn == 1:
            current_score = inning.player_one_score
            new_score = current_score + score
            inning.player_one_score = new_score
            session.query(Inning).filter(Inning.id == inning_id).update({'player_one_score':new_score})

        elif inning.player_turn == 2:
            current_score = inning.player_two_score
            new_score = current_score + score
            inning.player_two_score = new_score
            session.query(Inning).filter(Inning.id == inning_id).update({'player_two_score':new_score})
    

        new_dart_count = inning.dart_count + 1
        print(f"new_dart_count is {new_dart_count}")
        session.query(Inning).filter(Inning.id == inning_id).update({'dart_count':new_dart_count})

        inning_val_to_update = getattr(inning,col_to_mark)
        inning_val_current = inning_val_to_update + mark_update
        print(f"")
        session.query(Inning).filter(Inning.id == inning_id).update({col_to_mark:inning_val_current})
        
        inning_marks_set = set([ inning.p1_fifteen,    
                            inning.p1_sixteen,
                            inning.p1_seventeen,
                            inning.p1_eightteen,
                            inning.p1_nineteen,
                            inning.p1_twenty,
                            inning.p1_bullseye,

                            inning.p2_fifteen,
                            inning.p2_sixteen,
                            inning.p2_seventeen,
                            inning.p2_eightteen,
                            inning.p2_nineteen,
                            inning.p2_twenty,
                            inning.p2_bullseye,                    
                        ]) #Inning Marks is used to check if the game is over. 

        check_marks = all(marks >= 3 for marks in inning_marks_set)
        print(f"Are all the innings closed out? {check_marks}")
        
        if check_marks == True:
            session.query(Game).filter(Game.id == inning.game_id).update({'game_over':True})
            session.query(Inning).filter(Inning.id == inning_id).update({'game_over':True})

            if inning.player_one_score > inning.player_two_score:
                session.query(Game).filter(Game.id == inning.game_id).update({'winner_username':inning.player_one_username})
                session.query(Game).filter(Game.id == inning.game_id).update({'loser_username':inning.player_two_username})

            elif inning.player_one_score > inning.player_two_score:
                session.query(Game).filter(Game.id == inning.game_id).update({'winner_username':inning.player_two_username})
                session.query(Game).filter(Game.id == inning.game_id).update({'loser_username':inning.player_one_username})
            else:
                session.query(Game).filter(Game.id == inning.game_id).update({'winner_username':'draw'})   #This could be updated with a better pattern.
                session.query(Game).filter(Game.id == inning.game_id).update({'loser_username':'draw'})   #This could be updated with a better pattern.
            
            session.commit()
            return inning

        if new_dart_count >= 3:
            inning.inning = inning.inning + 1
            inning.dart_count = 0

            if inning.player_turn == 1:
                inning.player_turn = 2
            elif inning.player_turn == 2:
                inning.player_turn = 1

            print(f"Player turn now {inning.player_turn}")
            
            session.add(inning)
            


        session.commit()
        return inning

    finally:
        session.close()




        




