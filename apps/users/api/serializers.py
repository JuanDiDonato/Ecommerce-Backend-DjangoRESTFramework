# Rest framework serializers
from rest_framework import serializers

# Simple JWT 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Models
from apps.users.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['role'] = str(user.role)

        return token

# Serializer for create, edit, and delete users
class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('id','username','password','email','address')

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

class UserLogoutSerializer(serializers.ModelSerializer):
    class Meta : 
        model = User
        fields = ('username',)