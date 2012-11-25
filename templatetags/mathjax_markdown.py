from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

def mathrepl(matchobj):
    if matchobj.group(1) == r'\[':
        return r'<div>' + matchobj.group(0) + '</div>'
    else:
        retval = matchobj.group(0).replace('\\','\\\\')
        retval = re.sub(r'([][{}()_*#+-.!])',r'\\\1',retval)
        return retval

@register.filter
@stringfilter
def math_escape(value):
    retval = re.sub(r'(?s)(\\(?:\[|\()).*?(\\(?:\]|\)))',mathrepl,value)
    return retval

