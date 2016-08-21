from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from Chimera.models import ProfilePhoto
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def profile_photos(request):
    profile_photos_view = ProfilePhotosView()
    response = render(request, 'page/abstract/multi-listable.html', Context(profile_photos_view.get_elements()))
    return HttpResponse(response)


class ProfilePhotosView(MultiListableView):
    def __init__(self):
        current_profile_photos_list = ProfilePhoto.objects.all()

        title = ["Profile Photos", ]

        header = [
            ('ID', 'profile-photo', True),
            ('Album', 'album', False),
            ('User', 'user', True),
            ('Consumer', 'consumer', False),
            ('Chef', 'chef', False),
        ]

        entry = []

        for profile_photo in current_profile_photos_list:
            entry.append(
                [
                    (profile_photo.id, header[0]),
                    (profile_photo.album_id, header[1]),
                    (profile_photo.user_id, header[2]),
                    (profile_photo.consumer_id, header[3]),
                    (profile_photo.chef_id, header[4]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
