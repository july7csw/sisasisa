import re

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def addCss(value, keyword):
    text = value.replace(keyword, '<strong>' + keyword + '</strong>')
    text = mark_safe(text)
    return text
