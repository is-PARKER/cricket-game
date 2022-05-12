from enum import unique
from operator import index
from cricket.data.__db_session import session

import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from cricket.data.modelbase import Base




class User(Base):
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime())
    last_login = sqlalchemy.Column(sqlalchemy.DateTime())

    game = relationship("Game")
    inning = relationship("Inning")