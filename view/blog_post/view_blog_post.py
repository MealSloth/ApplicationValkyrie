from Valkyrie.form.blog_post.form_blog_post_edit import BlogPostEditForm
from Valkyrie.view.abstract.view_single_listable import SingleListableView
from Chimera.models import BlogPost, Blob, Author
from Chimera.settings import GCS_URL, PROTOCOL
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context


def blog_post(request, blog_post_id):
    blog_post_view = BlogPostView(blog_post_id=blog_post_id)
    response = render(request, 'page/abstract/single-listable.html', Context(blog_post_view.get_elements()))
    return HttpResponse(response)


class BlogPostView(SingleListableView):
    def __init__(self, blog_post_id):
        current_blog_post = BlogPost.objects.filter(pk=blog_post_id)
        if not current_blog_post.values().count() > 0:
            return
        else:
            current_blog_post = current_blog_post[0]

        blog_post_edit_button = [
                'fragment/modal/form/form-modal.html',                          # Modal template
                'fragment/modal/form/add-form/blog-post-add-edit-form.html',    # Form template
                BlogPostEditForm({                                              # Form instance
                    'author_id': current_blog_post.author_id,
                    'title': current_blog_post.title,
                    'short_description': current_blog_post.short_description,
                    'long_description': current_blog_post.long_description,
                }),
                current_blog_post.id,                                           # ID parameter for action
                'valkyrie-page-single-listable__blog-post-edit-modal',          # Modal ID
                'Edit Post',                                                    # Modal title text
                'btn btn-primary',                                              # Button style
                'blog-post-edit',                                               # Form action
                'Save Edit',                                                    # Submit button text
                'glyphicon glyphicon-pencil',                                   # Listable button style
                'valkyrie-fragment-form__section-form',                         # Form CSS class
                '',                                                             # Form enctype
            ]

        associated_items = ['Album', ]

        blog_post_delete_button = [
                'fragment/modal/delete-confirmation-modal.html',                                # Modal template
                '',                                                                             # Form template
                '',                                                                             # Form instance
                current_blog_post.id,                                                           # ID parameter
                'valkyrie-page-single-listable__blog-post-delete-modal',                        # Modal ID
                'Delete Blog Post',                                                             # Modal title text
                'btn btn-danger',                                                               # Button style
                'blog-post-delete',                                                             # Submit action
                'Delete Blog Post',                                                             # Submit button text
                'glyphicon glyphicon-trash',                                                    # Listable button style
                '',                                                                             # Form CSS class
                '',                                                                             # Form enctype
                'Deleting this blog post also deletes all of the following associated items:',  # Modal body header
                associated_items,                                                               # Modal body list
                'Are you sure you would like to delete this blog post?',                        # Modal body footer
            ]

        blog_post_buttons= [blog_post_edit_button, blog_post_delete_button, ]

        id = [('Blog Post', current_blog_post.id, blog_post_buttons), ]

        author = Author.objects.get(pk=current_blog_post.author_id)

        info = [
            ('Title', current_blog_post.title),
            ('Author', author.first_name + ' ' + author.last_name),
            ('Short Description', current_blog_post.short_description[:30] + ' ...'),
            ('Long Description', current_blog_post.long_description[:50] + ' ...'),
        ]

        id_pool = [
            ('Album ID', current_blog_post.album_id, 'album'),
        ]

        blobs = [PROTOCOL + GCS_URL, Blob.objects.filter(album_id=current_blog_post.album_id)]

        kwargs = {
            'id': id,
            'info': info,
            'id_pool': id_pool,
            'blobs': blobs,
        }

        SingleListableView.__init__(self, **kwargs)
