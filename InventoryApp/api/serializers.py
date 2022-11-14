from rest_framework import serializers
from shop.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        exclude = ("shelf_life",)