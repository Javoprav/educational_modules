from rest_framework import serializers
from edu_modules.models import Module


class ModulesSerializers(serializers.ModelSerializer):
    """Сериализатор для модели Module"""
    class Meta:
        model = Module
        fields = "__all__"
