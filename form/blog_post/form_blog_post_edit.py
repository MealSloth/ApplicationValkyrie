from _include.Chimera.Chimera.view.blog_post.view_blog_post_edit import blog_post_edit as edit_blog_post
from _include.Chimera.Chimera.models import Author
from django.forms import *


def authors():
    response = []
    for item in Author.objects.all().values():
        response.append((item.get('id'), item.get('first_name') + ' ' + item.get('last_name')))
    return tuple(response)


class BlogPostEditForm(Form):
    author_id = ChoiceField(choices=authors(), required=True)
    title = CharField(max_length=100, required=True)
    short_description = CharField(max_length=500, required=True)
    long_description = CharField(max_length=10000, required=True, widget=Textarea)

    def process(self, blog_post_id):
        blog_post_edit_kwargs = {
            'blog_post_id': blog_post_id,
            'author_id': self.cleaned_data['author_id'],
            'title': self.cleaned_data['title'],
            'short_description': self.cleaned_data['short_description'],
            'long_description': self.cleaned_data['long_description'],
        }

        edit_blog_post(request=None, **blog_post_edit_kwargs)
