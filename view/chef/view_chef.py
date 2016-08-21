from Valkyrie.view.abstract.view_single_listable import SingleListableView
from Chimera.models import Chef, User
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def chef(request, chef_id):
    chef_view = ChefView(chef_id=chef_id)
    response = render(request, 'page/abstract/single-listable.html', Context(chef_view.get_elements()))
    return HttpResponse(response)


class ChefView(SingleListableView):
    def __init__(self, chef_id):
        current_chef = Chef.objects.filter(pk=chef_id)
        if not current_chef.values().count() > 0:
            return
        else:
            current_chef = current_chef[0]

        id = [('Chef', current_chef.id), ]

        associated_user = User.objects.filter(pk=current_chef.user_id)

        if associated_user.values().count() > 0:
            associated_user = associated_user[0]
            info = [('Associated User', associated_user.first_name + ' ' + associated_user.last_name), ]
        else:
            info = []

        id_pool = [
            ('User ID', current_chef.user_id, 'user'),
            ('Location ID', current_chef.location_id, 'location'),
        ]

        kwargs = {
            'id': id,
            'info': info,
            'id_pool': id_pool,
        }

        SingleListableView.__init__(self, **kwargs)
