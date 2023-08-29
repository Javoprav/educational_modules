from django.contrib import admin
from .models import *


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updated_at',)
    list_filter = ('name',)
