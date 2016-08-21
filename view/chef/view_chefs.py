from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from Chimera.models import Chef
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def chefs(request):
    chefs_view = ChefsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(chefs_view.get_elements()))
    return HttpResponse(response)


class ChefsView(MultiListableView):
    def __init__(self):
        current_chefs_list = Chef.objects.all()

        title = ["Chefs", ]

        header = [
            ('ID', 'chef', True),
            ('User', 'user', False),
            ('Location', 'location', False),
        ]

        entry = []

        for chef in current_chefs_list:
            entry.append(
                [
                    (chef.id, header[0]),
                    (chef.user_id, header[1]),
                    (chef.location_id, header[2]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
