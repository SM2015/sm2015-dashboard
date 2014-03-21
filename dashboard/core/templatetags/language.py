from django import template
from django.conf import settings
register = template.Library()


@register.simple_tag
def current_lang(*args, **kwargs):
    return str(settings.LANGUAGE_CODE)
