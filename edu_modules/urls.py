from rest_framework.routers import DefaultRouter
from django.urls import path, include
from edu_modules.views import *
from django.views.decorators.cache import never_cache, cache_page

router = DefaultRouter()
router.register(r'edu_modules', ModulesViewSet, basename='edu_modules')


urlpatterns = [
    path('api/', include(router.urls)),
    path('', never_cache(IndexView.as_view()), name='Index'),
              ]
