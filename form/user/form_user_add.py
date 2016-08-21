from _include.Chimera.Chimera.view.user.view_user_create import user_create as create_user
from _include.Chimera.Chimera.models import User
from _include.Chimera.Chimera.enums import *
from datetime import datetime
from django.forms import *


def date(date_list):
    response = ""
    for item in date_list:
        if len(str(item)) < 2:
            response += "0" + item + "-"
        else:
            response += item + "-"
    response = response[:-1]
    response += "T00:00:00.000000"
    return response


def years():
    response = []
    now = datetime.utcnow()
    for i in range(1900, now.year + 1):
        response.append([i, str(i)])
    return tuple(response)


def days():
    response = []
    for i in range(1, 32):
        response.append([i, str(i)])
    return tuple(response)


class UserAddForm(Form):
    first_name = CharField(max_length=30, required=True)
    last_name = CharField(max_length=30, required=True)
    email = EmailField(max_length=254, required=True)
    phone_number = CharField(max_length=30, required=True)
    dob_year = ChoiceField(choices=years(), required=True)
    dob_month = ChoiceField(choices=Months.Months, required=True)
    dob_day = ChoiceField(choices=days(), required=True)
    gender = ChoiceField(choices=Gender.Gender, required=True)
    password = CharField(max_length=255, required=True, widget=PasswordInput())
    password_confirm = CharField(max_length=255, required=True, widget=PasswordInput())

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def clean(self):
        cleaned_data = super(UserAddForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if not password == password_confirm:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data

    def process(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        phone_number = self.cleaned_data['phone_number']
        gender = self.cleaned_data['gender']
        date_of_birth = date([
            self.cleaned_data['dob_year'],
            self.cleaned_data['dob_month'],
            self.cleaned_data['dob_day'],
        ])
        password = self.cleaned_data['password']

        user_kwargs = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number,
            'gender': gender,
            'date_of_birth': date_of_birth,
            'password': password,
        }

        create_user(request=None, **user_kwargs)

        user = User.objects.filter(email=email)
        if user.count() > 0:
            user = user[0]
            return user
        else:
            return
