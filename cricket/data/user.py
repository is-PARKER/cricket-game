from cricket.data.__db_session import session

import sqlalchemy
from cricket.data.modelbase import Base
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

# Need to setup flask-user
class User(Base,UserMixin):
    id = sqlalchemy.column(sqlalchemy.Integer,)