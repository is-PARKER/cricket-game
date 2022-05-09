from enum import unique
from operator import index
from cricket.data.__db_session import session

import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from cricket.data.modelbase import Base
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin


#Flask-user uses the instance for the object to call the .Column method. This code calls it directly. It may be necessary to import the call.
# Need to setup flask-user
class User(Base,UserMixin):
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,index=True)
    active = sqlalchemy.Column('is_active', sqlalchemy.Boolean(), nullable=False, server_default='1')
    username = sqlalchemy.Column(sqlalchemy.Text(32), nullable=False,index=True, unique=True)
    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    email = sqlalchemy.Column(sqlalchemy.String(255, collation='NOCASE'), nullable=False, unique=True)
    email_confirmed_at = sqlalchemy.Column(sqlalchemy.DateTime())
    password = sqlalchemy.Column(sqlalchemy.String(255), nullable=False, server_default='')
    # User information
    first_name = sqlalchemy.Column(sqlalchemy.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = sqlalchemy.Column(sqlalchemy.String(100, collation='NOCASE'), nullable=False, server_default='')
    # Define the relationship to Role via UserRoles
    roles = relationship('Role', secondary='userrole')

    #TODO: Insert the back reference with the games.

    game = relationship("Game")
    inning = relationship("Inning")