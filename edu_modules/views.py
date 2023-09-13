from rest_framework import viewsets
from edu_modules.models import Module
from edu_modules.serializers.serializers import ModulesSerializers
from users.models import UserRoles
from .pagination import ModulesPagination


class ModulesViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Module с помощью viewsets"""
    serializer_class = ModulesSerializers
    queryset = Module.objects.all()
    pagination_class = ModulesPagination

    def perform_create(self, serializer) -> None:
        """Сохраняет новому объекту владельца"""
        serializer.save(owner=self.request.user)
