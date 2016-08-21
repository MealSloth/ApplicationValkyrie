from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from Chimera.models import UserLogin
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def user_logins(request):
    user_logins_view = UserLoginsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(user_logins_view.get_elements()))
    return HttpResponse(response)


class UserLoginsView(MultiListableView):
    def __init__(self):
        current_user_logins_list = UserLogin.objects.all()

        title = ["User Logins", ]

        header = [
            ('ID', 'user-login', True),
        ]

        entry = []

        for user_login in current_user_logins_list:
            entry.append(
                [
                    (user_login.id, header[0]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
