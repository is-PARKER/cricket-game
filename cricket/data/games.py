from ast import Index
from email.policy import default
from enum import unique
from ntpath import realpath
from cricket.data.__db_session import session

import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from cricket.data.modelbase import Base



class Game(Base):
    __tablename__ = "game"

    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True,index=True,unique=True)
    latest_inning = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default=0) 
    player_one_username = sqlalchemy.Column(sqlalchemy.Text(32),sqlalchemy.ForeignKey('user.username'), nullable= False) # Setup secondary key. Validation
    player_two_username = sqlalchemy.Column(sqlalchemy.Text(32),sqlalchemy.ForeignKey('user.username'), nullable = False) #Setup secondary Key. Validation


    game_over = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)
    winner_username = sqlalchemy.Column(sqlalchemy.Text(32),ForeignKey("user.username")) # Setup secondary key. Should be pulled from game creation.
    loser_username = sqlalchemy.Column(sqlalchemy.Text(32),ForeignKey("user.username")) # Setup secondary key. Should be pulled from game creation.


    inning = relationship("Inning")
    #Consider if data will be cached on the user side with Json, or pickled and pushed to postgres

