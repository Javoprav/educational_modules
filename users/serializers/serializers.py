from rest_framework import serializers
from users.models import User


class ForAuthUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'city')


class ForCreateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
