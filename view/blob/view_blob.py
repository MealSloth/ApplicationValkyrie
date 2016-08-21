from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.settings import GCS_URL, PROTOCOL
from _include.Chimera.Chimera.models import Blob
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def blob(request, blob_id):
    blob_view = BlobView(blob_id=blob_id)
    response = render(request, 'page/abstract/single-listable.html', Context(blob_view.get_elements()))
    return HttpResponse(response)


class BlobView(SingleListableView):
    def __init__(self, blob_id):
        current_blob = Blob.objects.filter(pk=blob_id)
        if not current_blob.values().count() > 0:
            return
        else:
            current_blob = current_blob[0]

        image = [PROTOCOL + GCS_URL + current_blob.gcs_id, ]

        blob_delete_button = [
                'fragment/modal/delete-confirmation-modal.html',                                # Modal template
                '',                                                                             # Form template
                '',                                                                             # Form instance
                current_blob.id,                                                                # ID parameter
                'valkyrie-page-single-listable__blob-delete-modal',                             # Modal ID
                'Delete Blob',                                                                  # Modal title text
                'btn btn-danger',                                                               # Button style
                'blob-delete',                                                                  # Submit action
                'Delete Blob',                                                                  # Submit button text
                'glyphicon glyphicon-trash',                                                    # Listable button style
                '',                                                                             # Form CSS class
                '',                                                                             # Form enctype
                '',                                                                             # Modal body header
                '',                                                                             # Modal body list
                'Are you sure you would like to delete this blob?',                             # Modal body footer
            ]

        blob_buttons = [blob_delete_button, ]

        id = [('Blob', current_blob.id, blob_buttons), ]

        info = [
            ('Content-Type', current_blob.content_type),
            ('Date Created', current_blob.time),
        ]

        id_pool = [
            ('Album ID', current_blob.album_id, 'album'),
        ]

        kwargs = {
            'image': image,
            'id': id,
            'info': info,
            'id_pool': id_pool,
        }

        SingleListableView.__init__(self, **kwargs)
