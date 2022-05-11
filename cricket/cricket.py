from distutils.command.config import config
import os
import sys

import flask
from flask import Flask
import psycopg2

from cricket.data.users import User

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

import cricket.data.__db_session as db_session
import cricket.config

from flask_login import LoginManager


cricket = Flask(__name__)



if cricket.config["ENV"] == "production":
    cricket.config.from_object("config.ProductionConfig")
else:
    cricket.config.from_object("config.DevelopmentConfig")
print(f"App configuration is {cricket.config["ENV"]}")




username = 'username' #setup environmental variables.
password = 'password'




def main():
    configure()

def configure():

    login_manager = LoginManager()
    login_manager.init_app(cricket)

    register_blueprints()

    setup_db()

def setup_db(username,password):

    connection_string = 'postgresql+psycopg2://' + username + password + '@cricket-game/cricket'
    print(f'Connection String is {connection_string} ')

    db_session.database_init(connection_string)




if __name__ == '__main__':
    main()
else:
    configure()