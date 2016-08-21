from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from _include.Chimera.Chimera.models import Blob
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def blobs(request):
    blobs_view = BlobsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(blobs_view.get_elements()))
    return HttpResponse(response)


class BlobsView(MultiListableView):
    def __init__(self):
        current_blobs_list = Blob.objects.all().order_by('-time')

        title = ["Blobs", ]

        header = [
            ('ID', 'blob', True),
            ('Album ID', 'album', False),
            ('Content Type', '', False),
            ('Date Created', '', True),
        ]

        entry = []

        for blob in current_blobs_list:
            entry.append(
                [
                    (blob.id, header[0]),
                    (blob.album_id, header[1]),
                    (blob.content_type, header[2]),
                    (blob.time, header[3]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
