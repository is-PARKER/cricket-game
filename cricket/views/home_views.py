
import flask

from cricket.infrastructure.view_modifiers import response
from cricket.viewmodels.home.index_viewmodel import IndexViewModel
from cricket.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    vm = IndexViewmodel()
    return vm.to_dict()


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    vm = ViewModelBase()
    return vm.to_dict()