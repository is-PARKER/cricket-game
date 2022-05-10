
import flask
from flask import render_template
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin


from cricket.viewmodels.account.index_viewmodel import IndexViewModel
from cricket.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account')
@login_required()
def index():
    vm = IndexViewModel()
    return render_template('account/index.html', vm.to_dict())




