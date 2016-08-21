from django import template
from Chimera.enums import *

register = template.Library()


@register.simple_tag
def entry_for_post_status(dictionary):
    return PostStatus.PostStatus[int(dictionary.get("post_status"))][1]
