from Valkyrie.view.abstract.view_single_listable import SingleListableView
from Chimera.models import Consumer, User
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def consumer(request, consumer_id):
    consumer_view = ConsumerView(consumer_id=consumer_id)
    response = render(request, 'page/abstract/single-listable.html', Context(consumer_view.get_elements()))
    return HttpResponse(response)


class ConsumerView(SingleListableView):
    def __init__(self, consumer_id):
        current_consumer = Consumer.objects.filter(pk=consumer_id)
        if not current_consumer.values().count() > 0:
            return
        else:
            current_consumer = current_consumer[0]

        id = [('Consumer', current_consumer.id), ]

        associated_user = User.objects.filter(pk=current_consumer.user_id)

        if associated_user.values().count() > 0:
            associated_user = associated_user[0]
            info = [('Associated User', associated_user.first_name + ' ' + associated_user.last_name), ]
        else:
            info = []

        id_pool = [
            ('User ID', current_consumer.user_id, 'user'),
            ('Location ID', current_consumer.location_id, 'location'),
        ]

        kwargs = {
            'id': id,
            'info': info,
            'id_pool': id_pool,
        }

        SingleListableView.__init__(self, **kwargs)
