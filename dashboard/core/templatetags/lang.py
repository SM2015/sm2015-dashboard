from django import template
from django.conf import settings
register = template.Library()


@register.tag
def current_lang(*args, **kwargs):
    return settings.LANGUAGE_CODE
