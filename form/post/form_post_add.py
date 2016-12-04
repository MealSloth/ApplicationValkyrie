from Chimera.view.post.view_post_create import post_create as create_post
from Chimera.models import User, Chef
from django.forms import *


class PostAddForm(Form):
    name = CharField(max_length=50, required=True)
    summary = CharField(max_length=255, required=True)
    capacity = IntegerField(max_value=20)

    def process(self, user_id):
        user = User.objects.get(pk=user_id)
        chef = Chef.objects.get(user=user)
        post_create_kwargs = {
            'chef_id': chef.id,
            'name': self.cleaned_data['name'],
            'summary': self.cleaned_data['summary'],
            'capacity': self.cleaned_data['capacity'],
        }

        post = create_post(request=None, **post_create_kwargs)

        return post
