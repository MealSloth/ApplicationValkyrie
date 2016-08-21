from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from Valkyrie.form.user.form_user_add import UserAddForm
from Chimera.models import User
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def users(request):
    users_view = UsersView()
    response = render(request, 'page/abstract/multi-listable.html', Context(users_view.get_elements()))
    return HttpResponse(response)


class UsersView(MultiListableView):
    def __init__(self):
        current_users_list = User.objects.all().order_by('join_date')

        user_add_button = [
                'fragment/modal/form/form-modal.html',              # Modal template
                'fragment/modal/form/add-form/user-add-form.html',  # Form template
                UserAddForm(),                                      # Form instance
                '',                                                 # ID parameter for action
                'valkyrie-page-single-listable__user-add-modal',    # Modal ID
                'Add User',                                         # Modal title text
                'btn btn-primary',                                  # Button style
                'user-add',                                         # Form action
                'Add User',                                         # Submit button text
                'btn btn-primary pull-right',                       # Header button style
                'valkyrie-fragment-form__section-form',             # Form CSS class
                '',                                                 # Form enctype
            ]

        user_buttons = [user_add_button, ]

        title = ["Users", user_buttons, ]

        header = [
            ('ID', 'user', True),           # ('Column Title', 'URL parameter (if linked)', Boolean display on mobile)
            ('Name', '', False),
            ('Gender', '', False),
            ('Email', '', True),
            ('Phone Number', '', False),
            ('Date of Birth', '', False),
        ]

        entry = []

        for user in current_users_list:
            entry.append(
                [
                    (user.id, header[0]),                                   # (Entry, Corresponding header[] tuple)
                    (user.first_name + ' ' + user.last_name, header[1]),
                    (user.get_gender_display(), header[2]),
                    (user.email, header[3]),
                    (user.phone_number, header[4]),
                    (user.date_of_birth[:10], header[5]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
