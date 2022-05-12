
import flask
from flask import Request
from flask import render_template

from infrastructure.forms import RegisterUserForm, LoginForm
from infrastructure.cookie_auth import set_auth_username, logout
from services import user_service



from viewmodels.account.index_viewmodel import IndexViewModel
from viewmodels.shared.viewmodelbase import ViewModelBase



blueprint = flask.Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account')
def index():
    vm = IndexViewModel()
    return render_template('account/index.html', **vm.to_dict())


### Register ###

@blueprint.route('/account/register', methods=['GET','POST'])
def register():
    request_form = request.form
    form = RegisterUserForm(request_form)

    if request.method == 'POST' and form.validate():
        user = user_service.create_user(form.username.data,form.email.data,form.password.data)

        if not user:
            error = "User Invalid!"
    
        resp = flask.redirect('/account')
        set_auth_username(resp,user.username)
        
        return resp
    
    return render_template('account/register.html', form=form)

### Login ###

@blueprint.route('/account/login', method=['GET','POST'])
def login():

    request_form = request.form
    form = LoginForm(request_form)
    if request.method == 'POST' and form.validate():
        user = user_service.login_user(form.username.data,form.password.data)
        if not user:
            error = "The account does not exist or the password is wrong."
        
        resp = flask.redirect('/account')
        set_auth_username(resp, user.username)
        return resp

    return render_template('account/login.html', form=form)


### Logout ###

@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    logout(resp)
            





