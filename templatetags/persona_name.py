from django import template

register = template.Library()

@register.filter
def shortname(value):
    return value.split('@')[0]

