from django import template

register = template.Library()


@register.simple_tag
def active_css_class(request_path, app_url_path):
    
    split_request_path = request_path.split("/")
    if  split_request_path[1] == app_url_path:
        return "active"
    else:
        return ""