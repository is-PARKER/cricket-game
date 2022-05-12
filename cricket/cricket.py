import os
import sys

import flask
from flask import Flask
# import psycopg2


folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

import cricket.data.__db_session as db_session


import cricket.config

cricket = Flask(__name__)



if cricket.config["ENV"] == "production":
    cricket.config.from_object("config.ProductionConfig")
else:
    cricket.config.from_object("config.DevelopmentConfig")

# username = 'username' #setup environmental variables.
# password = 'password'

def main():
    configure()

def configure():

    register_blueprints()

    setup_db()

def setup_db(username,password):

    #connection_string = 'postgresql+psycopg2://' + username + password + '@cricket-game/cricket'
    # print(f'Connection String is {connection_string} ')
    connection_string = os.path.join(os.path.dirname(__file__),'db','test.sqlite')

    db_session.database_init(connection_string)

def register_blueprints():

    from cricket.views import account_views
    from cricket.views import game_views
    from cricket.views import home_views

    cricket.register_blueprint(account_views.blueprint)
    cricket.register_blueprint(game_views.blueprint)
    cricket.register_blueprint(home_views.blueprint)


if __name__ == '__main__':
    main()
else:
    configure()