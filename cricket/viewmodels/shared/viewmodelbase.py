from typing import Optional

import flask 
from flask import Request


class ViewModelBase:
    def __init__(self):
        self.request: Request = flask.request
        #consdier adding request dictionary. 

        self.error: Optional[str] = None
        self.user_id: Optional[int] = cookie_auth.get_user_id_via_auth_cookie(self.request)

    def to_dict(self):
        return self.__dict__