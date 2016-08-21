from django.forms import *


class LoginForm(Form):
    username = CharField(required=True, max_length=30, widget=TextInput(attrs={'placeholder': 'Username'}))
    password = CharField(required=True, widget=PasswordInput(attrs={'placeholder': 'Password'}))

    def process(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        return {'username': username, 'password': password}
