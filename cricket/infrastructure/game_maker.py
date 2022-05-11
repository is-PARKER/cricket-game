import hashlib 
from datetime import timedelta
from typing import Optional
from urllib import response

from flask import Request
from flask import Response



game_cookie_name ="cricket_game_cookie"

game_state = 

def set_game_inning(response: Response, game_id,latest_inning):
    
    resp = response.set_cookie(game_id,latest_inning)
    return response

def get_

def check_cookie_auth_username(request: Request) -> Optional:
    if auth_cookie_name not in request.cookies:
        return None
    
    username_cookie = request.cookies[auth_cookie_name]

    if len(username_cookie) != 2:
        return None

    username = username_cookie[0]
    username_hash = username_cookie[1]
    hash_check = text_hasher(username)

    if username_hash != hash_check:

        return None

    return username

def logout(response: Response) -> Response:
    response.delete_cookie(auth_cookie_name)
    return response