from Chimera.view.review.view_review_edit import review_edit as edit_review
from django.forms import *


class ReviewEditForm(Form):
    title = CharField(max_length=50, required=True)
    summary = CharField(max_length=500, required=True)
    rating = IntegerField(max_value=10)

    def process(self, review_id):
        review_edit_kwargs = {
            'review_id': review_id,
            'title': self.cleaned_data['title'],
            'summary': self.cleaned_data['summary'],
            'rating': self.cleaned_data['rating'],
        }

        review = edit_review(request=None, **review_edit_kwargs)

        return review
