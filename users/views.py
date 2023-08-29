from rest_framework import generics
from users.models import UserRoles
from users.serializers.serializers import *


class UsersListView(generics.ListAPIView):
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()


class UsersDetailView(generics.RetrieveAPIView):
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.id)


class UsersCreateView(generics.CreateAPIView):
    serializer_class = ForCreateUserSerializers
    queryset = User.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.id)


class UsersUpdateView(generics.UpdateAPIView):
    serializer_class = ForCreateUserSerializers
    queryset = User.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.id)
