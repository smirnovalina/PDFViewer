from django import template

register = template.Library()


@register.filter(name='split')
def split(line, splitter):
    return line.split(splitter)
