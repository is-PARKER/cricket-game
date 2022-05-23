from typing import Optional, List

import data.__db_session as db_session
import re 

from infrastructure.input_lists import mark_to_name,mark_score,mark_marker_count,other_name,mark_name_to_player
from services.user_service import find_user_by_username
from data.games import Game
from data.innings import Inning
from services import game_service, inning_service



def compute_dart(vm_object) -> Optional[Inning]:
    print(vm_object.to_dict())

    inning_id = vm_object.inning.id
    mark = vm_object.hit # Mark is the place where the board was hit. 
    

    to_mark_count = mark_marker_count[mark] # To mark count returns the mark count that will be applied.
    print(f"{mark} marks {to_mark_count}")

    mark_to_query_name = mark_to_name[mark] # Mark to the name needed for the query update. 
    print(f"{mark} sql entry is {mark_to_query_name}")

    other_query_name = other_name[mark] # This gives the other players mark name for query. 
    print(f"{mark} sql entry is {other_query_name}")

    player_inning_mark_count = get_inning_object_value(vm_object=vm_object, query_name=mark_to_query_name )
    other_player_inning_mark_count = get_inning_object_value(vm_object=vm_object, query_name=other_query_name)

    player_to_give_scores = mark_name_to_player[mark_to_query_name]

    if player_inning_mark_count >= 3 and other_player_inning_mark_count < 3:
        score = mark_score[mark] # Mark looks up dictionary with score.
        print(f"{player_to_give_scores} scored {score} points!")
        
    else:
        score = 0
        print(f"{player_to_give_scores} scored {score} points.")

    new_inning = inning_service.update_inning_by_dart(inning_id=inning_id, score=score, col_to_mark=mark_to_query_name,mark_update=to_mark_count)
    print(f"Inning updates: {new_inning.__str__()}")

    return new_inning

        

def get_inning_object_value(vm_object,query_name):
    inning_object = vm_object.inning
    
    inning_object_method_value = getattr(inning_object,query_name)
    print(f"inning object is {inning_object}. Value:{inning_object_method_value}")

    return inning_object_method_value


