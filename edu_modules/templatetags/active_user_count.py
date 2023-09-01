from django import template
from users.models import User
register = template.Library()


@register.simple_tag
def active_user_count():
    count = User.objects.filter(is_active=True).count()
    return f'{count} пользователей.'
