from django import template

register = template.Library()


@register.inclusion_tag(filename='tags/filter.html')
def dashboard_filter():
   pass