
from .models import Stock
from django import forms

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ("shelf_life","date","docs","storage","shelf_life","exp","attendant")
 

class StockAdminForms(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ("docs","storage","shelf_life","exp","attendant")
