from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from Valkyrie.form.blog_post.form_blog_post_add import BlogPostAddForm
from _include.Chimera.Chimera.models import BlogPost, Author
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context


def blog_posts(request):
    blog_posts_view = BlogPostsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(blog_posts_view.get_elements()))
    return HttpResponse(response)


class BlogPostsView(MultiListableView):
    def __init__(self):
        current_blog_posts_list = BlogPost.objects.all().order_by('-post_time')

        blog_post_add_button = [
                'fragment/modal/form/form-modal.html',                              # Modal template
                'fragment/modal/form/add-form/blog-post-add-edit-form.html',        # Form template
                BlogPostAddForm(),                                                  # Form instance
                '',                                                                 # ID parameter for action
                'valkyrie-page-single-listable__blog-post-add-modal',               # Modal ID
                'Make a Blog Post',                                                 # Modal title text
                'btn btn-primary',                                                  # Button style
                'blog-post-add',                                                    # Form action
                'Add Blog Post',                                                    # Submit button text
                'btn btn-primary pull-right',                                       # Header button style
                'valkyrie-fragment-form__section-form',                             # Form CSS class
                'multipart/form-data',                                              # Form enctype
            ]

        blog_post_buttons = [blog_post_add_button, ]

        title = ["Blog Posts", blog_post_buttons, ]

        header = [
            ('ID', 'blog-post', True),
            ('Title', '', True),
            ('Author', '', True),
            ('Short Description', '', False),
            ('Long Description', '', False),
        ]

        entry = []

        for blog_post in current_blog_posts_list:
            author = Author.objects.get(pk=blog_post.author_id)
            entry.append(
                [
                    (blog_post.id, header[0]),
                    (blog_post.title, header[1]),
                    (author.first_name + ' ' + author.last_name, header[2]),
                    (blog_post.short_description[:30] + ' ...', header[3]),
                    (blog_post.long_description[:40] + ' ...', header[4]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
