from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import Order
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def order(request, order_id):
    order_view = OrderView(order_id=order_id)
    response = render(request, 'page/abstract/single-listable.html', Context(order_view.get_elements()))
    return HttpResponse(response)


class OrderView(SingleListableView):
    def __init__(self, order_id):
        current_order = Order.objects.filter(pk=order_id)
        if not current_order.values().count() > 0:
            return
        else:
            current_order = current_order[0]

        order_delete_button = [
                'fragment/modal/delete-confirmation-modal.html',                            # Modal template
                '',                                                                         # Form template
                '',                                                                         # Form instance
                current_order.id,                                                           # ID parameter for action
                'valkyrie-page-single-listable__order-delete-modal',                        # Modal ID
                'Delete Order',                                                             # Modal title text
                'btn btn-danger',                                                           # Button style
                'order-delete',                                                             # Submit action
                'Delete Order',                                                             # Submit button text
                'glyphicon glyphicon-trash',                                                # Listable button style
                '',                                                                         # Form CSS class
                '',                                                                         # Form enctype
                '',                                                                         # Modal body header
                '',                                                                         # Modal body list
                'Are you sure you would like to delete this order?',                        # Modal body footer
            ]

        order_buttons = [order_delete_button, ]

        id = [('Order', current_order.id, order_buttons), ]

        info = [
            ('Order Type', current_order.get_order_type_display()),
            ('Amount', current_order.amount),
            ('Order Time', current_order.order_time[5:16].replace("T", " ")),
        ]

        widget = [('fragment/widget/single-listable/order-status-widget.html', current_order.order_status), ]

        id_pool = [
            ('Post ID', current_order.post_id, 'post'),
            ('Consumer ID', current_order.consumer_id, 'consumer'),
            ('Chef ID', current_order.chef_id, 'chef'),
            ('Location ID', current_order.location_id, 'location'),
            ('Billing ID', current_order.billing_id, 'billing'),
            ('Order Summary ID', current_order.order_summary_id, 'order-summary'),
        ]

        kwargs = {
            'id': id,
            'info': info,
            'widget': widget,
            'id_pool': id_pool,
        }

        SingleListableView.__init__(
            self, **kwargs
        )
