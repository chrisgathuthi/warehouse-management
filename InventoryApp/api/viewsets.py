from rest_framework import viewsets, mixins
from shop.models import Stock, Sales
from .serializers import StockSerializer, SalesSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "pk"

class StockGenericViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):

    """
    get -> list Qs
    get -> retrieve -> Product instance Detail view
    """

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "pk"

#stock_retreive_views = StockGenericViewset.as_view({"get":"retreive"})
#stock_list_views = StockGenericViewset.as_view({"get":"list"})

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    lookup_field = "pk"
