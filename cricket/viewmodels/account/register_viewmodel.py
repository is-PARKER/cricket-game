from services import user_service
from viewmodels.shared.viewmodelbase import ViewModelBase




class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.username = self.request.form['username']
        self.email = self.request.form['email'].lower().strip()
        self.password = self.request.form['password'].strip() 
    def validate(self):
        if not self.name or not self.name.strip():
            self.error = 'You must specify a name.'
        elif not self.email or not self.email.strip():
            self.error = 'You must specify a email.'
        elif not self.password:
            self.error = 'You must specify a password.'
        elif user_service.find_user_by_username(self.username):
            self.error = 'A user with that username address already exists.'
        elif user_service.find_user_by_email(self.email):
            self.error = 'A user with that email address already exists.'