from rest_framework import serializers
from edu_modules.models import Module
from edu_modules.validators import excludeValidator


class ModulesSerializers(serializers.ModelSerializer):
    """Сериализатор для модели Module"""
    class Meta:
        model = Module
        fields = "__all__"
        validators = [excludeValidator]
