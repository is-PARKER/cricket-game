import os
import sys

import flask
from flask import Flask


# import psycopg2


folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from data import __db_session as db_session


import config

cricket = Flask(__name__)



if cricket.config["ENV"] == "production":
    cricket.config.from_object("config.ProductionConfig")
else:
    cricket.config.from_object("config.DevelopmentConfig")

# username = 'username' #setup environmental variables.
# password = 'password'

def main():
    configure()
    cricket.run(debug=True, port=5006)

def configure():

    register_blueprints()

    setup_db()

def setup_db(): #might need username and pasword later.

    #connection_string = 'postgresql+psycopg2://' + username + password + '@cricket-game/cricket'
    # print(f'Connection String is {connection_string} ')
    connection_string = "sqlite:////" + os.path.join(os.path.dirname(__file__),'db','test.sqlite')

    db_session.database_init(connection_string)

def register_blueprints():

    from views import account_views
    from views import game_views
    from views import home_views

    cricket.register_blueprint(account_views.blueprint)
    cricket.register_blueprint(game_views.blueprint)
    cricket.register_blueprint(home_views.blueprint)


if __name__ == '__main__':
    main()
else:
    configure()