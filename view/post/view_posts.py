from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from _include.Chimera.Chimera.models import Post
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def posts(request):
    posts_view = PostsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(posts_view.get_elements()))
    return HttpResponse(response)


class PostsView(MultiListableView):
    def __init__(self):
        current_posts_list = Post.objects.all().order_by('-post_time')

        title = ["Posts", ]

        header = [
            ('ID', 'post', True),
            ('Name', '', True),
            ('Order Count', '', False),
            ('Capacity', '', False),
            ('Status', '', False),
            ('Expire Time', '', False),
        ]

        entry = []

        for post in current_posts_list:
            entry.append(
                [
                    (post.id, header[0]),
                    (post.name, header[1]),
                    (post.order_count, header[2]),
                    (post.capacity, header[3]),
                    (post.get_post_status_display(), header[4]),
                    (post.expire_time, header[5]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
