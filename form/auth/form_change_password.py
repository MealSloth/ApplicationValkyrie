from django.contrib.auth.models import User
from django.forms import *


class ChangePasswordForm(Form):
    password = CharField(required=True, widget=PasswordInput(attrs={'placeholder': 'Password'}))
    password_confirm = CharField(required=True, widget=PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    def process(self, auth_user_id):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if password == password_confirm:
            pass
        else:
            return

        user = User.objects.get(pk=auth_user_id)

        user.set_password(password)

        user.save()
