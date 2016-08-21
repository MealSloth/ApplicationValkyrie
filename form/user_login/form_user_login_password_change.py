from _include.Chimera.Chimera.view.user_login.view_user_login_password_change import user_login_password_change as change_user_login_password
from django.forms import *


class UserLoginPasswordChangeForm(Form):
    password = CharField(required=True, widget=PasswordInput)
    password_confirm = CharField(required=True, widget=PasswordInput)

    def process(self, user_login_id):
        if not self.cleaned_data['password'] == self.cleaned_data['password_confirm']:
            raise ValidationError('Passwords do not match')

        user_login_password_change_kwargs = {
            'user_login_id': user_login_id,
            'password': self.cleaned_data['password'],
        }

        user_login = change_user_login_password(request=None, **user_login_password_change_kwargs)

        return user_login
