from rest_framework import viewsets
from edu_modules.models import Module
from edu_modules.serializers.serializers import ModulesSerializers
from .pagination import ModulesPagination


class ModulesViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Module с помощью viewsets"""
    serializer_class = ModulesSerializers
    queryset = Module.objects.all()
    pagination_class = ModulesPagination
