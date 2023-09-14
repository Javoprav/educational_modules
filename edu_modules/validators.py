from rest_framework import serializers
from datetime import time


def excludeValidator(value):
    """Валидатор на минимальное описание"""
    if len(value.get('description')) < 100:
        raise serializers.ValidationError('Минимальное описание 100 символов')
