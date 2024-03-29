
from rest_framework import generics, permissions, authentication
from .serializers import StockSerializer, UserSerializer
from shop.models import Stock
from .permissions import IsStaffEditorPermissions
from api.authentication import TokenAuthentication
import datetime
# Create your views here.
class StockCreateView(generics.CreateAPIView):

    """create stock api"""

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    authentication_classes = [authentication.SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.shelf_life = datetime.timedelta(days=10,hours=10,minutes=50)
        serializer.save(attendant = self.request.user, shelf_life =serializer.shelf_life)



class StockListView(generics.ListCreateAPIView):
    """list all stock api"""       

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_authenticated:
            return Stock.objects.none()
        return qs.filter(attendant=user)


class StockRetrieveView(generics.RetrieveAPIView):
    """get stock api"""       

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class StockUpdateView(generics.UpdateAPIView):
    """stock update api"""

    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDeleteView(generics.DestroyAPIView):

    """stock delete api"""

    queryset = Stock.objects.all()
    serializer_class = StockSerializer


