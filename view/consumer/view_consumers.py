from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from _include.Chimera.Chimera.models import Consumer
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def consumers(request):
    consumers_view = ConsumersView()
    response = render(request, 'page/abstract/multi-listable.html', Context(consumers_view.get_elements()))
    return HttpResponse(response)


class ConsumersView(MultiListableView):
    def __init__(self):
        current_consumers_list = Consumer.objects.all()

        title = ["Consumers", ]

        header = [
            ('ID', 'consumer', True),
            ('User', 'user', False),
            ('Location', 'location', False),
        ]

        entry = []

        for consumer in current_consumers_list:
            entry.append(
                [
                    (consumer.id, header[0]),
                    (consumer.user_id, header[1]),
                    (consumer.location_id, header[2]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
