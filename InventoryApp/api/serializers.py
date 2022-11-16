from rest_framework import serializers
from django.contrib.auth.models import User

from shop.models import Stock

class UserSerializer(serializers.ModelSerializer):
    stock = serializers.PrimaryKeyRelatedField(many=True,queryset=Stock.objects.all())
    class Meta:
        model = User
        fields = ["id", "username", "stock"]


class StockSerializer(serializers.ModelSerializer):
    attendant = serializers.ReadOnlyField(source = "attendant.username")
    class Meta:
        model = Stock
        exclude = ("shelf_life",)