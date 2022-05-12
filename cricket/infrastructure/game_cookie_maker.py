import hashlib 
from datetime import timedelta
from typing import Optional 
from urllib import response

from flask import Request
from flask import Response



def set_game_cookies(response: Response, game_id, latest_inning, p1_username):
    

    resp = response

    resp.set_cookie('game_id', game_id)
    resp.set_cookie('latest_inning',latest_inning)
    resp.set_cookie('game_p1', p1_username)

    return resp

def check_username_match(request: Request, viewmodel_username) -> bool:

    cookies = request.cookies

    if 'game_p1' not in cookies:
        return False

    if cookies.get('game_p1') == viewmodel_username:
        return True
    

def delete_game_cookies(response: Response) -> Response:
    response.delete_cookie('game_id')
    response.delete_cookie('latest_inning')
    response.delete_cookie('game_p1')

    return response