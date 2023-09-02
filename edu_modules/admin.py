from django.contrib import admin
from .models import Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    """Админка для отображения модулей"""
    list_display = ('id', 'name', 'updated_at',)
    list_filter = ('name',)
