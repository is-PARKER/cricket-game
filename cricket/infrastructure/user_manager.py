import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

from cricket.data.modelbase import Base
from cricket.cricket import cricket
from cricket.data.users import User

user_manager = UserManager(cricket,Base,User)