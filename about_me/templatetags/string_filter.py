from django import template

register = template.Library()


@register.filter
def replace_at(value):
    return value.replace("@", "(at)")


@register.filter
def replace_dot(value):
    return value.replace(".", "(dot)")