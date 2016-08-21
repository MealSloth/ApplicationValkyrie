from _include.Chimera.Chimera.view.order.view_order_create import order_create as create_order
from _include.Chimera.Chimera.models import Consumer, User
from _include.Chimera.Chimera.enums import OrderType
from django.forms import *


def consumers():
    response = []
    for user in User.objects.all().values():
        if Consumer.objects.filter(pk=user.get('consumer_id')).count() > 0:
            response.append((user.get('consumer_id'), user.get('first_name') + ' ' + user.get('last_name')))
    return tuple(response)


class OrderAddForm(Form):
    consumer_id = ChoiceField(choices=consumers(), required=True)
    order_type = ChoiceField(choices=OrderType.OrderType)
    amount = IntegerField()

    def process(self, post_id):
        order_create_kwargs = {
            'post_id': post_id,
            'consumer_id': self.cleaned_data['consumer_id'],
            'order_type': self.cleaned_data['order_type'],
            'amount': self.cleaned_data['amount'],
        }

        order = create_order(request=None, **order_create_kwargs)

        return order
