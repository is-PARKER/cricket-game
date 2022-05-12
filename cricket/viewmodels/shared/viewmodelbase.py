from typing import Optional

import flask 
from flask import Request

from infrastructure.cookie_auth import check_cookie_auth_username


class ViewModelBase:
    def __init__(self):
        self.request: Request = flask.request
        #consdier adding request dictionary. 

        self.error: Optional[str] = None
        self.username: Optional[int] = check_cookie_auth_username(self.request)

    def to_dict(self):
        return self.__dict__