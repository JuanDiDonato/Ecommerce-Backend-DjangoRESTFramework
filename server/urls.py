# Django
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

# Rest framework
from rest_framework import permissions
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Views
from apps.users.views import Login, Logout, RefreshTokenView, Register, mercado_pago

# Permissions
from apps.users.authenticate import RoleAuthentication
# Swagger
schema_view = get_schema_view(
    openapi.Info(
      title="E-Commerce REST API",
      default_version='v0.1',
      description="REST API para un ecommerce.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="juan_didonato@protonmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(RoleAuthentication,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('register/',authentication_classes([])(permission_classes([AllowAny])(Register)).as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('admin/', admin.site.urls),
    path('checkout/', mercado_pago, name='checkout'),
    path('client/',include('apps.client.api.routers')),
    path('products/',include('apps.products.api.routers')),
    path('mod/',include('apps.mod.api.routers'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)