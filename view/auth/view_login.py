from django.contrib.auth import authenticate, login as user_login
from django.http import HttpResponse, HttpResponseRedirect
from Valkyrie.form.auth.form_login import LoginForm
from django.template import Context
from django.shortcuts import render


def login(request):
    reply = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            credentials = form.process()
            user = authenticate(username=credentials.get('username'), password=credentials.get('password'))
            if user is not None:
                if user.is_active:
                    user_login(request=request, user=user)
                    return HttpResponseRedirect('/')
                else:
                    reply = 'Please contact an administrator'
            else:
                reply = 'Invalid credentials'
        else:
            reply = 'Invalid credentials'

    response = render(request, 'page/auth/login.html', Context({'form': LoginForm(), 'reply': reply}))
    return HttpResponse(response)
