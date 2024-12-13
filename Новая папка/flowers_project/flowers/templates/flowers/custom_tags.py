from django import template
from flowers.models import Type

register = template.Library()

@register.simple_tag
def all_types():
    return Type.objects.all()
