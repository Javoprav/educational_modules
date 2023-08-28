from rest_framework.routers import DefaultRouter
from django.urls import path
from edu_modules.views import *

router = DefaultRouter()
router.register(r'edu_modules', ModulesViewSet, basename='edu_modules')


urlpatterns = [
    path('modules/', ModulesListView.as_view(), name='modules_list'),
              ] + router.urls
