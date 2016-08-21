from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from _include.Chimera.Chimera.models import Post, Review
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def reviews(request):
    reviews_view = ReviewsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(reviews_view.get_elements()))
    return HttpResponse(response)


class ReviewsView(MultiListableView):
    def __init__(self):
        reviews_list = Review.objects.all().order_by('-time')

        title = ["Reviews", ]

        header = [
            ('ID', 'review', True),
            ('Rating', '', True),
            ('Title', '', True),
            ('Time', '', False),
        ]

        entry = []

        for review in reviews_list:
            entry.append(
                [
                    (review.id, header[0]),
                    (review.rating, header[1]),
                    (review.title, header[2]),
                    (review.time, header[3]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
