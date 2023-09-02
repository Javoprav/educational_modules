from rest_framework.routers import DefaultRouter
from django.urls import path, include
from edu_modules.views import ModulesViewSet

router = DefaultRouter()
router.register(r'edu_modules', ModulesViewSet, basename='edu_modules')

urlpatterns = [
    path('', include(router.urls)),
]
