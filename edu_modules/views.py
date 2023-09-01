from rest_framework import viewsets
from edu_modules.models import Module
from edu_modules.serializers.serializers import ModulesSerializers
from .pagination import ModulesPagination
from django.views.generic import TemplateView
from random import sample


class ModulesViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Module с помощью viewsets"""
    serializer_class = ModulesSerializers
    queryset = Module.objects.all()
    pagination_class = ModulesPagination


class IndexView(TemplateView):
    """Главная страница"""
    template_name = 'edu_modules/index.html'
    extra_context = {
        'title': 'Главная страница',
        'object_list': Module.objects.all()
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_posts = list(Module.objects.all())
        context['random_modules'] = sample(all_posts, min(3, len(all_posts)))
        return context
