from Valkyrie.form.blog_post.form_blog_post_add import BlogPostAddForm
from _include.Chimera.Chimera.settings import PROTOCOL
from django.http import HttpResponseRedirect


def blog_post_add(request):
    if request.method == 'POST':
        form = BlogPostAddForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.process()
            return HttpResponseRedirect(PROTOCOL + 'mealsloth.com/blog-post/%s' % str(blog_post.id))

    return HttpResponseRedirect('/blog-posts')
