from _include.Chimera.Chimera.view.blog_post.view_blog_post_delete import blog_post_delete as delete_blog_post
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def blog_post_delete(request, blog_post_id):
    blog_post_delete_kwargs = {'blog_post_id': blog_post_id}
    try:
        delete_blog_post(request=None, **blog_post_delete_kwargs)
        return HttpResponseRedirect('/blog-posts')
    except StandardError:
        return HttpResponseRedirect(reverse('blog-post', args=[blog_post_id, ]))
