from Chimera.view.post.view_post_delete import post_delete as delete_post
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def post_delete(request, post_id):
    post_delete_kwargs = {'post_id': post_id}
    try:
        delete_post(request=None, **post_delete_kwargs)
    except StandardError:
        return HttpResponseRedirect(reverse('post', args=[post_id, ]))
    return HttpResponseRedirect('/posts')
