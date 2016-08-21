from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from Chimera.models import Location
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def locations(request):
    locations_view = LocationsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(locations_view.get_elements()))
    return HttpResponse(response)


class LocationsView(MultiListableView):
    def __init__(self):
        current_locations_list = Location.objects.all()

        title = ["Locations", ]

        header = [
            ('ID', 'location', True),
            ('User', 'user', False),
            ('Purpose', '', False),
            ('Type', '', False),
            ('Address', '', True),
        ]

        entry = []

        for location in current_locations_list:
            entry.append(
                [
                    (location.id, header[0]),
                    (location.user_id, header[1]),
                    (location.get_purpose_display(), header[2]),
                    (location.get_type_display(), header[3]),
                    (
                        location.address_line_one +
                        ' ' +
                        location.address_line_two +
                        ', ' +
                        location.city +
                        ', ' +
                        location.state +
                        ' ' +
                        location.country,
                        header[4]
                    ),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
