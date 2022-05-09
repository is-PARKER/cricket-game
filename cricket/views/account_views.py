
import flask

from cricket.infrastructure.view_modifiers import response
from cricket.viewmodels.home.index_viewmodel import IndexViewModel
from cricket.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    return vm.to_dict()


@blueprint.route('/account/login')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    return vm.to_dict()

@blueprint.route('/account/logout')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    return vm.to_dict()


