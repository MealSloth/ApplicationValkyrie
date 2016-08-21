from Valkyrie.form.review.form_review_edit import ReviewEditForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def review_edit(request, review_id):
    if request.method == 'POST':
        form = ReviewEditForm(request.POST)
        if form.is_valid():
            review = form.process(review_id)
            return HttpResponseRedirect(reverse('review', args=[review.id, ]))
        else:
            return HttpResponseRedirect(reverse('post', args=[review_id, ]))

    return HttpResponseRedirect(reverse('post', args=[review_id, ]))
