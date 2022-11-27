from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework.reverse import reverse
from shop.models import Stock, Sales


class SalesSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(many=True, read_only= True)
    class Meta:
        model = Sales
        fields = ["item","employee", "stock_sold","stock_qty","date"]
class UserSerializer(serializers.ModelSerializer):
    stock = serializers.PrimaryKeyRelatedField(many=False,queryset=Stock.objects.all())
    class Meta:
        model = User
        fields = ["id", "username", "stock"]


class StockSerializer(serializers.ModelSerializer):
    attendant = serializers.ReadOnlyField(source = "attendant.username")
    item = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="sales-detail")
    #email = serializers.EmailField(write_only=True)
    class Meta:
        model = Stock
        fields = ["product_name", 
            "item",
            "pk",
            #"email",
            "attendant",
            "net_weight",
            "qty",
            "date",
            "isle",
            "tags",
            "storage", 
            "exp",
            "attendant",
            "status",
            ]
    # def create(self, validated_data):
    #     email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     print(obj,email)
    #     return obj
    # def validate_status(self, value):
    #     qs = Stock.objects.filter(status__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already used as a status")
    #     return value
        

        

    # def get_url(self,obj):
    #     request = self.context.get("request")#many serializers don't have request
    #     if request is None:
    #         return None
    #     return reverse("stock-retrieve-api",kwargs={"obj":obj.pk},request=request)