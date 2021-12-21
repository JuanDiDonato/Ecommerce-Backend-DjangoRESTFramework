# DJango
from django.contrib.auth import authenticate
from django.conf import settings

# Rest Framework
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Simple JWT
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

# Serializer
from apps.users.api.serializers import CustomTokenObtainPairSerializer
from apps.users.api.serializers import UserSerializer

# Models
from apps.users.models import User

# Register
class Register(GenericAPIView):
    serializer_class = UserSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error':True, 'message':serializer.errors },status=status.HTTP_400_BAD_REQUEST)

# Login
class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self,request,*args,**kwargs):
        response = Response()
        # Obtiene el username del request, sino lo setea vacio.
        username = request.data.get('username','')
        password = request.data.get('password', '')
        # Devuelte true o false si hay un user y password asociado en la db
        user = authenticate(username=username,password=password)

        if user:
            login_serializer = self.serializer_class(data=request.data) # genera el token
            if login_serializer.is_valid():
                user_serializer = UserSerializer(user) # devuelve el user
                # Creo la cookie
                response.set_cookie(
                    key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                    value = login_serializer.validated_data.get('access'),
                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                #csrf.get_token(request)
                # agrego los datos del usuario y el refresh token
                response.data = {
                    'refresh_token':login_serializer.validated_data.get('refresh'),
                    'user':user_serializer.data
                    }
                return response
                """
                return Response({
                    'token':login_serializer.validated_data.get('access'),
                    'refresh_token':login_serializer.validated_data.get('refresh'),
                    'user':user_serializer.data
                },status=status.HTTP_200_OK)
                """
            return Response({'Error':'Usuario o contraseña incorrectos'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'Error':'Usuario o contraseña incorrectos'},status=status.HTTP_400_BAD_REQUEST)

# Logout
class Logout(GenericAPIView):
    serializer_class = UserSerializer

    """
    **Tokens en headers

    Para el logout, primero obtengo el usuario.
    Si existe, refresco su token, pero no lo retorno ni lo seteo.
    """
    def post(self,request,*args,**kwargs):
        response = Response()
        user = User.objects.filter(id=request.data.get('user',0))
        if user.exists():
            """        
            For tokens in headers 

            RefreshToken.for_user(user.first())
            """
            # Para cerrar sesion, borro lo cookie
            response.delete_cookie('access_token')
            response.data = {'message':'Session cerrada correctamente.'}
            return response
        return Response({'message':'A ocurrido un error inesperado.'},status=status.HTTP_400_BAD_REQUEST)

class RefreshTokenView(TokenViewBase):
    serializer_class = serializers.TokenRefreshSerializer

    # Sobreescribo el metodo post de TokenViewBase
    def post(self, request, *args, **kwargs):
        response = Response()
        serializer = self.get_serializer(data=request.data)
        # Si actualiza el token, que actualize la cookie
        try:
            serializer.is_valid(raise_exception=True)
            response.set_cookie('access_token',serializer.validated_data['access'])
            response.data = {'refresh_token': serializer.validated_data['refresh'],'message':'Token actualizado.'}
        except TokenError as e:
            response.data = {'error':True}
            raise InvalidToken(e.args[0])

        return response