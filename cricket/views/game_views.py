
import flask
from flask import redirect, render_template
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

from cricket.viewmodels.game.index_viewmodel import IndexViewModel
from cricket.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint('game', __name__, template_folder='templates')


### Index has most the ability to search through the games.

@blueprint.route('/game', method=['GET'])
@login_required()
def index():
    vm = IndexViewModel()
    if not vm.user:
        return redirect('login')
    return render_template(template_file='game/index.html', **vm.to_dict())

@login_required()
@blueprint.route('/game', method=['POST'])
def index():
    vm = IndexViewModel()
    return render_template(template_file='game/index.html', **vm.to_dict())



### Create Game View ###    
@blueprint.route('/game/create', method=['GET'])
@login_required()
def create():
    vm = CreateGameViewModel()
    return render_template(template_file='game/create.html', **vm.to_dict())

@blueprint.route('/game/create', method=['POST'])
@login_required()
def create():
    vm = CreateGameViewModel()
    return render_template(template_file='game/create.html', **vm.to_dict())



### Play Game ###
@blueprint.route('/game/play', method=['GET'])
@login_required()
def play():
    vm = PlayGameViewModel()
    return render_template(template_file='game/play.html', **vm.to_dict())

@blueprint.route('/game/play', method=['POST'])
@login_required()
def play():
    vm = PlayGameViewModel()
    return render_template(template_file='game/play.html', **vm.to_dict())


### TODO: Create Review Later ###