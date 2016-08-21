from django.http import HttpResponseRedirect, HttpResponse
from Valkyrie.form.post.form_post_add import PostAddForm
from django.core.urlresolvers import reverse


def post_add(request, user_id):
    if request.method == 'POST':
        form = PostAddForm(request.POST)
        if form.is_valid():
            post = form.process(user_id=user_id)
            return HttpResponseRedirect(reverse('post', args=[post.id, ]))
        else:
            return HttpResponse("Invalid form")
    else:
        return HttpResponseRedirect(reverse('user', args=[user_id, ]))
