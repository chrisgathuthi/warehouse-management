from rest_framework.routers import DefaultRouter

from api.viewsets import StockViewSet, StockGenericViewset, SalesViewSet

router = DefaultRouter()
router.register("stock",StockGenericViewset,basename="stocks")
router.register("sales",SalesViewSet,basename="sales")
urlpatterns = router.urls