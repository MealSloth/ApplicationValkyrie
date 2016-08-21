from _include.Chimera.Chimera.view.order.view_order_delete import order_delete as delete_order
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def order_delete(request, order_id):
    order_delete_kwargs = {'order_id': order_id}
    try:
        post = delete_order(request=None, **order_delete_kwargs)
    except StandardError:
        return HttpResponseRedirect(reverse('order', args=[order_id, ]))

    return HttpResponseRedirect(reverse('post', args=[post.id, ]))
