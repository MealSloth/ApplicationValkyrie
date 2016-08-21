from Valkyrie.form.order.form_order_add import OrderAddForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def order_add(request, post_id):
    if request.method == 'POST':
        form = OrderAddForm(request.POST)
        if form.is_valid():
            order = form.process(post_id)
            return HttpResponseRedirect(reverse('order', args=[order.id, ]))
        else:
            return HttpResponseRedirect('/orders')
    else:
        return HttpResponseRedirect('/orders')
