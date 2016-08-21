from django.http import HttpResponseRedirect

from Valkyrie.form.blog_post.form_blog_post_edit import BlogPostEditForm
from _include.Chimera.Chimera.settings import PROTOCOL


def blog_post_edit(request, blog_post_id):
    if request.method == 'POST':
        form = BlogPostEditForm(request.POST)
        if form.is_valid():
            form.process(blog_post_id)
            return HttpResponseRedirect(PROTOCOL + 'mealsloth.com/blog/')
        else:
            return HttpResponseRedirect('/blogs')

    return HttpResponseRedirect('/blogs')
