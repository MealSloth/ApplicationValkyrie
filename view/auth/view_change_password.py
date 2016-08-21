from Valkyrie.form.auth.form_change_password import ChangePasswordForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            form.process(request.user.id)
            return HttpResponseRedirect('/')
    else:
        form = ChangePasswordForm()

    return render(request, 'page/auth/change-password.html', {'form': form})
