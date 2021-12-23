# Rest framework routers
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny


# ViewSets
from apps.products.views import  ProductViewSet, CategoryViewSet, EventViewSet, ColorViewSet, WaistViewSet, ImagesViewSet

router = DefaultRouter()  # Instance of DefaultRouter

router.register(r'products',authentication_classes([])(ProductViewSet),basename='products')
router.register(r'colors',ColorViewSet,basename='colors')
router.register(r'waist',WaistViewSet,basename='waist')
router.register(r'categories',CategoryViewSet,basename='categories')
router.register(r'events',EventViewSet,basename='events')
router.register(r'images',ImagesViewSet,basename='images')

urlpatterns = router.urls