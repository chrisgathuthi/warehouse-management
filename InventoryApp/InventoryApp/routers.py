from rest_framework.routers import DefaultRouter

from api.viewsets import StockViewSet, StockGenericViewset

router = DefaultRouter()
router.register("stock",StockGenericViewset,basename="stocks")

urlpatterns = router.urls