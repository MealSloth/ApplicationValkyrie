from _include.Chimera.Chimera.view.review.view_review_create import review_create as create_review
from _include.Chimera.Chimera.models import Post, Consumer, User
from django.forms import *


def consumers():
    response = []
    for user in User.objects.all().values():
        if Consumer.objects.filter(pk=user.get('consumer_id')).count() > 0:
            response.append((user.get('consumer_id'), user.get('first_name') + ' ' + user.get('last_name')))
    return tuple(response)


class ReviewAddForm(Form):
    consumer_id = ChoiceField(choices=consumers(), required=True)
    title = CharField(max_length=50, required=True)
    summary = CharField(max_length=255, required=False)
    rating = IntegerField(max_value=20)

    def process(self, post_id):
        post = Post.objects.get(pk=post_id)
        review_create_kwargs = {
            'post_id': post.id,
            'consumer_id': self.cleaned_data['consumer_id'],
            'rating': self.cleaned_data['rating'],
            'title': self.cleaned_data['title'],
            'summary': self.cleaned_data['summary'],
        }

        review = create_review(request=None, **review_create_kwargs)

        return review
