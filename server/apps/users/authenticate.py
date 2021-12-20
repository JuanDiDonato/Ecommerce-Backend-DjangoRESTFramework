# Settings of DJango
from django.conf import settings

# Rest framework
from rest_framework import exceptions, permissions

# Simple JWT
from rest_framework_simplejwt.authentication import JWTAuthentication

# Clase para verificar los tokens en la cookie
class CookieAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        
        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token

# Protege las vistas de Mod, solo acceden si tienen el rol de Admin.
class RoleAuthentication(permissions.BasePermission, JWTAuthentication):

    def has_permission(self, request, view):
        header = self.get_header(request)
        
        if header is None:
            # Obtengo el token de la cookie
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return False

        validated_token = self.get_validated_token(raw_token)

        if validated_token['role'] == 'Admin':
            return True
        return False

class MethodAndrRoleAuthentication(permissions.BasePermission, JWTAuthentication):

    def has_permission(self, request, view):

        header = self.get_header(request)
        
        if header is None:
            # Obtengo el token de la cookie
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return False

        validated_token = self.get_validated_token(raw_token)

        if request.method == 'POST' and validated_token['role'] != 'Admin':
            return False
        elif request.method == 'DELETE' and validated_token['role'] != 'Admin':
            return False
        elif request.method == 'PUT' and validated_token['role'] != 'Admin':
            return False
        elif request.method == 'PATCH' and validated_token['role'] != 'Admin':
            return False
        return True



