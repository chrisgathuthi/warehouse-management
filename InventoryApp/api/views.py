
from rest_framework import generics
from .serializers import StockSerializer
from shop.models import Stock

# Create your views here.
class StockCreateView(generics.CreateAPIView):

    """create stock api"""

    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def perform_create(self,serializer):
        serializer.save(attendant = self.request.user)



class StockListView(generics.ListAPIView):
    """list all stock api"""       

    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockUpdateView(generics.UpdateAPIView):
    """stock update api"""

    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDeleteView(generics.DestroyAPIView):
    """stock delete api"""
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

