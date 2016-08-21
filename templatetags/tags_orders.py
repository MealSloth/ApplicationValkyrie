from django import template
from _include.Chimera.Chimera.enums import *

register = template.Library()


@register.simple_tag
def entry_for_order_status(dictionary):
    return OrderStatus.OrderStatus[int(dictionary.get('order_status'))][1]


@register.simple_tag
def entry_for_order_type(dictionary):
    return OrderType.OrderType[int(dictionary.get('order_type'))][1]
