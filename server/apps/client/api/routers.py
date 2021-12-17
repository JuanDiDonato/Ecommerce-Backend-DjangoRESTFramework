# Rest framework routers
from rest_framework.routers import DefaultRouter

# ViewSets
from apps.client.views import ShoppingCartViewSet, ShoppingHistoryViewSet

router = DefaultRouter()  # Instance of DefaultRouter

router.register(r'shopping_cart',ShoppingCartViewSet,basename='cart')
router.register(r'shopping_history',ShoppingHistoryViewSet,basename='history')

urlpatterns = router.urls