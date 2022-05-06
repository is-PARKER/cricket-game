from enum import unique
from cricket.data.__db_session import session

import sqlalchemy
from cricket.data.modelbase import Base
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin


#Flask-user uses the instance for the object to call the .Column method. This code calls it directly. It may be necessary to import the call.
# Need to setup flask-user
class Roles(Base):
    __tablename__ = 'roles'

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    role = sqlalchemy.Column(sqlalchemy.String(50),unique=True)

