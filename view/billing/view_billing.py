from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import Billing, User
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def billing(request, billing_id):
    billing_view = BillingView(billing_id=billing_id)
    response = render(request, 'page/abstract/single-listable.html', Context(billing_view.get_elements()))
    return HttpResponse(response)


class BillingView(SingleListableView):
    def __init__(self, billing_id):
        current_billing = Billing.objects.filter(pk=billing_id)
        if not current_billing.values().count() > 0:
            return
        else:
            current_billing = current_billing[0]

        id = [('Billing', current_billing.id), ]

        associated_user = User.objects.filter(pk=current_billing.user_id)

        if associated_user.values().count() > 0:
            associated_user = associated_user[0]
            info = [('Associated User', associated_user.first_name + ' ' + associated_user.last_name), ]
        else:
            info = []

        id_pool = [
            ('User ID', current_billing.user_id, 'user'),
            ('Consumer ID', current_billing.consumer_id, 'consumer'),
            ('Chef ID', current_billing.chef_id, 'chef'),
            ('Location ID', current_billing.location_id, 'location'),
        ]

        kwargs = {
            'id': id,
            'info': info,
            'id_pool': id_pool,
        }

        SingleListableView.__init__(self, **kwargs)
