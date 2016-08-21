from Chimera.view.blob.view_blob_delete import blob_delete as delete_blob
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def blob_delete(request, blob_id):
    blob_delete_kwargs = {'blob_id': blob_id}
    try:
        delete_blob(request=None, **blob_delete_kwargs)
    except StandardError:
        return HttpResponseRedirect(reverse('blob', args=[blob_id, ]))
    return HttpResponseRedirect('/albums')
