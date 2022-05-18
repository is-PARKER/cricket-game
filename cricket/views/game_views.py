
from crypt import methods
import flask
from flask import redirect, render_template, Request
from services.user_service import find_user_by_username
from services.game_logic_service import compute_dart
from services import inning_service
from infrastructure.input_lists import hits_list

from infrastructure import game_cookie_maker
from infrastructure.forms import CreateGameForm

from viewmodels.game.creategame_viewmodel import CreateGameViewModel
from viewmodels.game.playgame_viewmodel import PlayGameViewmodel
from viewmodels.game.index_viewmodel import IndexViewmodel
from viewmodels.shared.viewmodelbase import ViewModelBase



blueprint = flask.Blueprint('game', __name__, template_folder='templates')

### Index has most the ability to search through the games.

@blueprint.route('/game', methods=['GET'])
def index_get():
    vm = IndexViewmodel()
    if not vm.username:
        return flask.redirect('/account/login')
    return render_template('game/index.html', **vm.to_dict())

@blueprint.route('/game', methods=['POST'])
def index_post():
    vm = IndexViewmodel()
    if not vm.username:
        return flask.redirect('/account/login')
    return render_template('game/index.html', **vm.to_dict())



### Create Game View ###    
@blueprint.route('/game/create', methods=['GET'])
def creategame_get():
    vm = CreateGameViewModel()
    request_form = vm.request.form
    form = CreateGameForm(request_form)
    vm.form = form
    if not vm.username:
        return flask.redirect('/account/login')
    return render_template('game/create.html', **vm.to_dict())

@blueprint.route('/game/create', methods=['POST'])
def creategame_post():
    vm = CreateGameViewModel()
    if not vm.username:
        return flask.redirect('/account/login')

    request_form = vm.request.form
    form = CreateGameForm(request_form)
    vm.form = form
    if form.validate() and find_user_by_username(form.player_two_username.data):
        from services.game_service import create_game_with_inning
        game = create_game_with_inning(player_one_username=vm.player_one_username , player_two_username=form.player_two_username.data)
        game_id = game.id

        resp = flask.redirect(f'/game/play/{game_id}')
        game_cookie_maker.set_game_cookies(response=resp, game_id=game.id,latest_inning=0,p1_username=vm.username)
        return resp

    if not find_user_by_username(form.player_two_username.data):
        vm.error_p2 = 'Player Two username could not be found!'

    return render_template('game/create.html', **vm.to_dict())


@blueprint.route('/game/review/<int:game_id>',methods=['GET','POST'])
def game_review(game_id: int):
    vm = PlayGameViewmodel(game_id)
    print(vm.game_id)
    if vm.username != vm.inning.player_one_username:
        resp = flask.redirect('/account')
        return resp

    return render_template('game/review.html', **vm.to_dict())


### Play Game ###
@blueprint.route('/game/play/<int:game_id>', methods=['GET'])
def play_get(game_id:int):
    vm = PlayGameViewmodel(game_id)
    print(vm.game_id)
    if vm.username != vm.inning.player_one_username:
        resp = flask.redirect('/account')
        return resp

    return render_template('game/play.html', **vm.to_dict())

@blueprint.route('/game/play/<int:game_id>', methods=['POST'])
def play_post(game_id:int):
    vm = PlayGameViewmodel(game_id)
    form = vm.request.form
    if form.get('dart_throw') in hits_list:
        vm.hit = form.get('dart_throw')
        vm.inning = compute_dart(vm_object=vm) 
    
    if vm.game.game_over == True:
        game_id = vm.game_id
        resp = flask.redirect('/game/review/<int:game_id>')
        return resp
        
    if vm.username != vm.inning.player_one_username:
        resp = flask.redirect('/account')
        return resp


    return render_template('game/play.html', **vm.to_dict())


### TODO: Create Review Later ###