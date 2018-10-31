from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True

@register.filter(name='addv')
def addv(field, value):
    return field.as_widget(attrs={"value":value})