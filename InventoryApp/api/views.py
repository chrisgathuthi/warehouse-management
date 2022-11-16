
from rest_framework import generics, permissions, authentication
from .serializers import StockSerializer, UserSerializer
from shop.models import Stock

# Create your views here.
class StockCreateView(generics.CreateAPIView):

    """create stock api"""

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(attendant = self.request.user)



class StockListView(generics.ListAPIView):
    """list all stock api"""       

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StockUpdateView(generics.UpdateAPIView):
    """stock update api"""

    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDeleteView(generics.DestroyAPIView):

    """stock delete api"""

    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class UserListView(generics.ListAPIView):

    """user list api """

    queryset = Stock.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):

    """user detail api"""

    queryset = Stock.objects.all()
    serializer_class = UserSerializer
