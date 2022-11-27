from django import forms
from django.contrib.auth.models import AbstractUser

from .models import Stock, Sales


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ("shelf_life","date","docs","storage","shelf_life","exp","attendant")

 

class StockAdminForms(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ("docs","storage","shelf_life","exp","attendant")

class SalesAdminForms(forms.ModelForm):
    class Meta:
        model = Sales
        fields = "__all__"
