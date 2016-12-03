from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from Chimera.models import Order
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def orders(request):
    orders_view = OrdersView()
    response = render(request, 'page/abstract/multi-listable.html', Context(orders_view.get_elements()))
    return HttpResponse(response)


class OrdersView(MultiListableView):
    def __init__(self):
        current_orders_list = Order.objects.all().order_by('-order_time')

        title = ["Orders", ]

        header = [
            ('ID', 'order', True),
            ('Consumer', 'consumer', False),
            ('Status', '', True),
            ('Type', '', True),
            ('Amount', '', True),
            ('Order Time', '', False),
        ]

        entry = []

        for order in current_orders_list:
            entry.append(
                [
                    (order.id, header[0]),
                    (order.consumer_id, header[1]),
                    (order.get_order_status_display(), header[2]),
                    (order.get_order_type_display(), header[3]),
                    (order.amount, header[4]),
                    (order.order_time, header[5]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
