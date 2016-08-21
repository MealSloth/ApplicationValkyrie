from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import Location, User
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def location(request, location_id):
    location_view = LocationView(location_id=location_id)
    response = render(request, 'page/abstract/single-listable.html', Context(location_view.get_elements()))
    return HttpResponse(response)


class LocationView(SingleListableView):
    def __init__(self, location_id):
        current_location = Location.objects.filter(pk=location_id)
        if not current_location.values().count() > 0:
            return
        else:
            current_location = current_location[0]

        id = [('Location', current_location.id), ]

        associated_user = User.objects.filter(pk=current_location.user_id)

        if associated_user.values().count() > 0:
            associated_user = associated_user[0]
            info = [('Associated User', associated_user.first_name + ' ' + associated_user.last_name), ]
        else:
            info = []

        info.append(('Purpose', current_location.get_purpose_display()))
        info.append(('Type', current_location.get_type_display()))

        info.append(('', '---'))

        if current_location.address_line_one:
            info.append(('', current_location.address_line_one))
        if current_location.address_line_two:
            info.append(('', current_location.address_line_two))
        if current_location.city:
            info.append(('', current_location.city))
        if current_location.state:
            info.append(('', current_location.state))
        if current_location.country:
            info.append(('', current_location.country))
        if current_location.zip:
            info.append(('', current_location.zip))

        id_pool = [
            ('User ID', current_location.user_id, 'user'),
        ]

        kwargs = {
            'id': id,
            'info': info,
            'id_pool': id_pool,
        }

        SingleListableView.__init__(self, **kwargs)
