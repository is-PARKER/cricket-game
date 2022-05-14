from ntpath import realpath
import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


from data.modelbase import Base





class Game(Base):
    __tablename__ = "game"

    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True,index=True,unique=True)
    latest_inning = sqlalchemy.Column(sqlalchemy.Integer, nullable = False, default=0) 
    player_one_username = sqlalchemy.Column(sqlalchemy.Text(32), nullable= False) # Setup secondary key. Validation
    player_two_username = sqlalchemy.Column(sqlalchemy.Text(32), nullable = False) #Setup secondary Key. Validation


    game_over = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)
    winner_username = sqlalchemy.Column(sqlalchemy.Text(32)) # Setup secondary key. Should be pulled from game creation.
    loser_username = sqlalchemy.Column(sqlalchemy.Text(32)) # Setup secondary key. Should be pulled from game creation.

    
    
    innings = relationship("Inning", back_populates="game")

   