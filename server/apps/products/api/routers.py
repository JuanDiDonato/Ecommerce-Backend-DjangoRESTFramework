from rest_framework.routers import DefaultRouter

# ViewSets
from apps.products.views import  ProductViewSet, CategoryViewSet, EventViewSet, ColorViewSet, WaistViewSet

router = DefaultRouter()  # Instance of DefaultRouter

router.register(r'products',ProductViewSet,basename='products')
router.register(r'colors',ColorViewSet,basename='colors')
router.register(r'waist',WaistViewSet,basename='waist')
router.register(r'categories',CategoryViewSet,basename='categories')
router.register(r'events',EventViewSet,basename='events')

urlpatterns = router.urls