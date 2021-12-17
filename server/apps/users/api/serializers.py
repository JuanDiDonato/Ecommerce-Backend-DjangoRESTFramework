from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Models
from apps.users.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

# Serializer for create, edit, and delete users
class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('id','username','email','address','role')

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Encrypt password
        user.save()
        return user

    def update(self,instance,validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
