from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsModerator(BasePermission):
    message = 'Доступ закрыт'

    def has_permission(self, request, view):
        if view.action in ['create', 'list', 'retrieve'] and request.user.is_authenticated:
            return True
        elif request.user.is_anonymous:
            return False
        elif view.action not in ['create', 'list', 'retrieve'] and request.user.is_staff or request.user.is_superuser or request.user.role == UserRoles.MODERATOR:
            return True
        return False
