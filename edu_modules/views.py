from rest_framework import viewsets
from edu_modules.models import Module
from edu_modules.serializers.serializers import ModulesSerializers
from .pagination import ModulesPagination
from .permissions import IsModerator


class ModulesViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Module с помощью viewsets"""
    serializer_class = ModulesSerializers
    queryset = Module.objects.all()
    pagination_class = ModulesPagination
    permission_classes = [IsModerator]

    def perform_create(self, serializer) -> None:
        """Сохраняет новому объекту владельца"""
        serializer.save(owner=self.request.user)
