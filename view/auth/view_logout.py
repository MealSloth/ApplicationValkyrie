from django.http import HttpResponseRedirect
from django.contrib.auth import logout as user_logout


def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/login')
