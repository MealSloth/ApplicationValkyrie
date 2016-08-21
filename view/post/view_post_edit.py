from Valkyrie.form.post.form_post_edit import PostEditForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def post_edit(request, post_id):
    if request.method == 'POST':
        form = PostEditForm(request.POST)
        if form.is_valid():
            post = form.process(post_id)
            return HttpResponseRedirect(reverse('post', args=[post.id, ]))
        else:
            return HttpResponseRedirect(reverse('post', args=[post_id, ]))

    return HttpResponseRedirect(reverse('post', args=[post_id, ]))
