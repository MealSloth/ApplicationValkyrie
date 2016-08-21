from Valkyrie.form.review.form_review_add import ReviewAddForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def review_add(request, post_id):
    if request.method == 'POST':
        form = ReviewAddForm(request.POST)
        if form.is_valid():
            review = form.process(post_id=post_id)
            return HttpResponseRedirect(reverse('review', args=[review.id, ]))
        else:
            return HttpResponse("Invalid form")
    else:
        return HttpResponseRedirect(reverse('post', args=[post_id, ]))
