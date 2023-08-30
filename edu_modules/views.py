from rest_framework import viewsets, generics
from edu_modules.models import Module
from edu_modules.serializers.serializers import ModulesSerializers


class ModulesViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Module с помощью viewsets"""
    serializer_class = ModulesSerializers
    queryset = Module.objects.all()
    # pagination_class = ModulesPagination

    # def perform_create(self, serializer) -> None:
    #     """Сохраняет новому объекту владельца"""
    #     serializer.save(owner=self.request.user)
    #
    # def get_queryset(self):
    #     """Выводит список модулей для разных пользователей"""
    #     user = self.request.user
    #     if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
    #         return Module.objects.all()
    #     else:
    #         return Module.objects.filter(owner=user)