import hashlib 
from datetime import timedelta
from posixpath import split
from typing import Optional
from urllib import response

from flask import Request
from flask import Response



auth_cookie_name ="cricket_cookie"


def set_auth_username(response: Response, username: str):
    hashed_username = text_hasher(username)
    hashed_dict = "{}:{}".format(username,hashed_username)
    print(hashed_dict)

    response.set_cookie(key=auth_cookie_name,value=hashed_dict, secure=False, httponly=True, samesite='lax')
    return response    

def text_hasher(text: str):

    salted = 'blahblah' + text + 'moreblah'
    hashed = hashlib.sha512(salted.encode('utf-8')).hexdigest()

    return hashed

def check_cookie_auth_username(request: Request):
    if auth_cookie_name not in request.cookies:
        print("Cookie not in Request")
        return None
    
    username_cookie = request.cookies[auth_cookie_name]
    print(username_cookie)

    split_cookie = username_cookie.split(':')
    if len(split_cookie) != 2:
        print("Cookie not long enough")
        return None

    username = split_cookie[0]
    username_hash = split_cookie[1]
    hash_check = text_hasher(username)

    if username_hash != hash_check:
        print(f"username not valid")
        return None

    print(f"username is {username}")
    return username

def logout_username(response: Response) -> Response:
    response.delete_cookie(auth_cookie_name)
    return response