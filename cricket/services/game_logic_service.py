from typing import Optional

import data.__db_session as db_session

from services.user_service import find_user_by_username
from data.games import Game
from data.innings import Inning
from services import game_service

def compute_dart(vm_dictionary):
    print(vm_dictionary.to_dict())

    if vm_dictionary.hit == "p1_miss" or "p2_miss":

        print("Miss")


def turn_update():
    #Check Closeout:
    
    #Updae for game:
        #Update LAtest Inning
        

