from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from .models import Ikan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data.get('role', 'pembeli')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class IkanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ikan
        fields = '__all__'
