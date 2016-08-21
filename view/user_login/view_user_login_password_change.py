from Valkyrie.form.user_login.form_user_login_password_change import UserLoginPasswordChangeForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def user_login_password_change(request, user_login_id):
    if request.method == 'POST':
        form = UserLoginPasswordChangeForm(request.POST)
        if form.is_valid():
            user_login = form.process(user_login_id)
            return HttpResponseRedirect(reverse('user-login', args=[user_login.id, ]))
        else:
            return HttpResponseRedirect(reverse('user-login', args=[user_login_id, ]))
    else:
        return HttpResponseRedirect(reverse('user-login', args=[user_login_id, ]))
