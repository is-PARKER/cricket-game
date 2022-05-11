import hashlib 
from datetime import timedelta
from pydoc import text
from typing import Optional
from urllib import response

from flask import Request
from flask import Response



auth_cookie_name ="cricket_cookie"

def set_auth_username(response: Response, username: str):
    hashed_username = text_hasher(username)
    hashed_dict = "{}:{}".format(username,hashed_username)

    response.set_cookie(key=auth_cookie_name,value=hashed_dict, secure=False, httponly=True, samesite='lax')
    return response

def text_hasher(text: str):
    hasher = hashlib.new('sha512')
    salted = 'blahblah' + text + 'moreblah'
    salted_and_hash = hasher.update(salted.encode('utf-8'))
    digested = salted_and_hash.hexdigest()
    return digested

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