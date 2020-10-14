from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def addCss(value, keyword):
    valueLower = value.lower()
    keywordLower = value.lower()
    keywordLength = len(keyword)
    keywordIndex = valueLower.find(keywordLower)
    keywordPart = value[keywordIndex:keywordIndex+keywordLength]
    keywordText = "<strong>" + keywordPart + "</strong>"
    finalText = value.replace(keywordPart, keywordText)
    return mark_safe(finalText)
