from Chimera.storage_url_suffixes import StorageURLSuffixes
from Chimera.view.blob.view_blob_upload import blob_upload as upload_blob
from base64 import b64encode
from django.forms import *


def url_suffixes():
    response = []
    dictionary = StorageURLSuffixes.get_url_suffixes()
    for key in dictionary:
        response.append([key, dictionary.get(key)])
    return tuple(response)


class BlobAddForm(Form):
    url_suffix = ChoiceField(choices=url_suffixes(), required=True)
    image = FileField(required=True)

    def process(self, album_id):
        image = self.cleaned_data['image']
        url_suffix = self.cleaned_data['url_suffix']

        blob_upload_kwargs = {
            'file': b64encode(image.read()),
            'album_id': str(album_id),
            'url_suffix': StorageURLSuffixes.get_url_suffix(storage_url_suffix=url_suffix),
        }

        upload_blob(request=None, **blob_upload_kwargs)
