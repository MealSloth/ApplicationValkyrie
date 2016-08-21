from Valkyrie.form.user.form_user_add import UserAddForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def user_add(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.process()
            return HttpResponseRedirect(reverse('user', args=[user.id, ]))
    return HttpResponseRedirect('/users')
