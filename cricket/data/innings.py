import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from  data.modelbase import Base



# Rounds holds game state which is loaded by python program. 

class Inning(Base):
    __tablename__ = "inning"

    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True,index=True)
    
    player_one_username = sqlalchemy.Column(sqlalchemy.Text(32), nullable =  False) # Set u p secondary key. Should be pulled from game creation.
    player_two_username = sqlalchemy.Column(sqlalchemy.Text(32), nullable = False) #Set u p secondary Key. Validation needed on creation.
    game_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("game.id"),  nullable = False) 

    game = relationship("Game")

    player_one_score = sqlalchemy.Column(sqlalchemy.Integer,  nullable = False, default = 0)
    player_two_score = sqlalchemy.Column(sqlalchemy.Integer,  nullable = False, default = 0)  
    scrubbed = sqlalchemy.Column(sqlalchemy.Boolean, default = False )
    player_turn = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 1)

    inning = sqlalchemy.Column(sqlalchemy.Integer,  nullable  = False, default=0) # needs updated in the game as progressed. 


    dart_count = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)

    # State to manage scoring and closeouts. 
    # Player one inning state.

    p1_fifteen = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p1_sixteen = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p1_seventeen = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p1_eightteen = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p1_nineteen = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p1_twenty = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p1_bullseye = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p1_miss = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)

    # Player two inning state.

    p2_fifteen = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p2_sixteen = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p2_seventeen = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p2_eightteen = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p2_nineteen = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p2_twenty = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p2_bullseye = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)
    p2_miss = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default = 0)




