from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.settings import GCS_URL, PROTOCOL
from Valkyrie.form.blob.form_blob_add import BlobAddForm
from _include.Chimera.Chimera.models import Album, Blob
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def album(request, album_id):
    album_view = AlbumView(album_id=album_id)
    response = render(request, 'page/abstract/single-listable.html', Context(album_view.get_elements()))
    return HttpResponse(response)


class AlbumView(SingleListableView):
    def __init__(self, album_id):
        current_album = Album.objects.filter(pk=album_id)
        if not current_album.values().count() > 0:
            return
        else:
            current_album = current_album[0]

        id = [('Album', current_album.id), ]

        info = [('Date Created', current_album.time), ]

        blobs_list = Blob.objects.filter(album_id=current_album.id)

        blobs_array = []

        for i in range(0, blobs_list.count()):
            blobs_array.append(blobs_list[i].id)

        blob_add_button = [
                'fragment/modal/form/form-modal.html',              # Modal template
                'fragment/modal/form/add-form/blob-add-form.html',  # Form template
                BlobAddForm(),                                      # Form instance
                current_album.id,                                   # ID parameter for action
                'valkyrie-page-single-listable__blob-add-modal',    # Modal ID
                'Add Blob',                                         # Modal title text
                'btn btn-primary',                                  # Button style
                'blob-add',                                         # Form action
                'Add Blob',                                         # Submit button text
                'glyphicon glyphicon-plus',                         # Listable button style
                'valkyrie-fragment-form__section-form',             # Form CSS class
                'multipart/form-data',                              # Form enctype
            ]

        blob_buttons = [blob_add_button, ]

        listable = [
            ('Blobs', blobs_array, 'blob', '', blob_buttons),
        ]

        blobs = [PROTOCOL + GCS_URL, blobs_list]

        kwargs = {
            'id': id,
            'info': info,
            'listable': listable,
            'blobs': blobs,
        }

        SingleListableView.__init__(self, **kwargs)
