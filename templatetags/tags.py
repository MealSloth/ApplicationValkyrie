from django import template


register = template.Library()


@register.simple_tag
def generate_link_with_key(dictionary, key, page_name):
    return "<a href=\"/" + page_name + "/" + dictionary.get(key) + "\">" + dictionary.get(key) + "</a>"


@register.simple_tag
def entry_for_key(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def entry_for_date(dictionary, key):
    return dictionary.get(key)[:-16]
