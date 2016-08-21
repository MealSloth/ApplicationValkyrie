from Chimera.view.review.view_review_delete import review_delete as delete_review
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def review_delete(request, review_id):
    review_delete_kwargs = {'review_id': review_id}
    try:
        delete_review(request=None, **review_delete_kwargs)
    except StandardError:
        return HttpResponseRedirect(reverse('review', args=[review_id, ]))
    return HttpResponseRedirect('/reviews')
