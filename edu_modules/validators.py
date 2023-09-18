from rest_framework import serializers


def excludeValidator(value):
    """Валидатор на минимальное описание"""
    if value.get('description') is None or len(value.get('description')) < 100:
        raise serializers.ValidationError('Минимальное описание 100 символов')
