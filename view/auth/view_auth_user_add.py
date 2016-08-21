from django.http import HttpResponseRedirect
from django.shortcuts import render
from Valkyrie.form.auth.form_auth_user_add import AuthUserAddForm


def auth_user_add(request):
    if request.method == 'POST':
        form = AuthUserAddForm(request.POST)
        if form.is_valid():
            form.process()
            return HttpResponseRedirect('/')
    else:
        form = AuthUserAddForm()

    return render(request, 'page/auth/auth-user-add.html', {'form': form})
