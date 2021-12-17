from rest_framework.routers import DefaultRouter

# ViewSets
from apps.mod.views import PendingShipmentsViewSet, StatisticViewSet, MonthlyStatisticViewSet

router = DefaultRouter()  # Instance of DefaultRouter

router.register(r'pending_shipments',PendingShipmentsViewSet,basename='pending_shipments')
router.register(r'statistics',StatisticViewSet,basename='statistics')
router.register(r'monthly_statistics',MonthlyStatisticViewSet,basename='monthly_statistics')


urlpatterns = router.urls