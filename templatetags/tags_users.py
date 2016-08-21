from django import template
from Chimera.enums import *


register = template.Library()


@register.simple_tag
def entry_for_user_gender(dictionary):
    return Gender.Gender[int(dictionary.get("gender"))][1]


@register.simple_tag
def status_for_status(status):
    return PostStatus.PostStatus[int(status)][1]


@register.simple_tag
def status_for_status_lower(status):
    return str(PostStatus.PostStatus[int(status)][1]).lower()