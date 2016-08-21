from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from _include.Chimera.Chimera.models import Billing
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def billings(request):
    billings_view = BillingsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(billings_view.get_elements()))
    return HttpResponse(response)


class BillingsView(MultiListableView):
    def __init__(self):
        current_billings_list = Billing.objects.all()

        title = ["Billings", ]

        header = [
            ('ID', 'billing', True),
            ('User', 'user', False),
            ('Chef', 'chef', False),
            ('Consumer', 'consumer', False),
            ('Location', 'location', False),
        ]

        entry = []

        for billing in current_billings_list:
            entry.append(
                [
                    (billing.id, header[0]),
                    (billing.user_id, header[1]),
                    (billing.chef_id, header[2]),
                    (billing.consumer_id, header[3]),
                    (billing.location_id, header[4]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
