from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.filter(name='mark')
def mark(result):
    percent = int(result['correct_answer_count'] / result['question_count'] * 100)
    mark = 2
    if percent > 80:
        mark = 5
    elif percent > 60:
        mark = 4
    elif percent > 40:
        mark = 3

    return mark


@register.filter(name='first_name')
def first_name(username):
    return User.objects.get(username=username).first_name


@register.filter(name='last_name')
def last_name(username):
    return User.objects.get(username=username).last_name
