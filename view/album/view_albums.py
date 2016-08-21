from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from Chimera.models import Album, Blob
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def albums(request):
    albums_view = AlbumsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(albums_view.get_elements()))
    return HttpResponse(response)


class AlbumsView(MultiListableView):
    def __init__(self):
        current_albums_list = Album.objects.all().order_by('-time')

        title = ["Albums", ]

        header = [
            ('ID', 'album', True),
            ('Date Created', '', True),
        ]

        entry = []

        for album in current_albums_list:
            entry.append(
                [
                    (album.id, header[0]),
                    (album.time, header[1]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
