
import flask
from flask import redirect, render_template, Request

from infrastructure import game_cookie_maker
from services.game_service import create_game
from infrastructure.forms import CreateGameForm
from viewmodels.game.index_viewmodel import IndexViewModel
from viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint('game', __name__, template_folder='templates')


### Index has most the ability to search through the games.

@blueprint.route('/game', method=['GET'])
def index():
    vm = IndexViewModel()
    if not vm.user:
        return flask.redirect('account/login')
    return render_template(template_file='game/index.html', **vm.to_dict())

@blueprint.route('/game', method=['POST'])
def index():
    vm = IndexViewModel()
    return render_template(template_file='game/index.html', **vm.to_dict())



### Create Game View ###    
@blueprint.route('/game/create', method=['GET','POST'])
def create():
    vm = CreateGameViewModel()
    req = request.form
    form = CreateGameForm(req)
    if request.method == "POST":
        
        game = services.create_game(p1_username = vm.player_one_username ,p2_username=form.player_two_username.data)

        resp = flask.redirect('playgame/< game.id >')
        game_cookie_maker.set_game_cookies(response=resp, game_id=game.id,latest_inning=0,p1_username=vm.username)
        

    return render_template(template_file='game/create.html', **vm.to_dict())




### Play Game ###
@blueprint.route('/game/play', method=['GET'])
def play():
    vm = PlayGameViewModel()
    return render_template(template_file='game/play.html', **vm.to_dict())

@blueprint.route('/game/play', method=['POST'])
def play():
    vm = PlayGameViewModel()
    return render_template(template_file='game/play.html', **vm.to_dict())


### TODO: Create Review Later ###