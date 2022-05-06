from logging import raiseExceptions
import sqlalchemy as sqal
from sqlalchemy import orm

from cricket.data.modelbase import Base

__session

# Session maker follows the Flask and Sqlalchemy session creation and factory creation pattern

def session_maker(connection: str):
    global __session

    if __session:
        return

    if not connection:
        return raiseExceptions("The connection path has not been passed to the session_maker")

    engine = sqal.engine.create_engine(connection)
    __session = orm.sessionmaker(engine)
    
    Base.metadata.create_all(engine)

def session():
    global __session

    session: Session = __session()

    return session