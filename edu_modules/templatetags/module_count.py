from django import template
from edu_modules.models import Module
register = template.Library()


@register.simple_tag
def module_count():
    count = Module.objects.all().count()
    return f'{count} модулей'

