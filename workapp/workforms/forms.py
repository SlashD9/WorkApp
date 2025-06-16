from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    class Meta :
        model = Stock
        fields = ["qty","item","description","location","cost_price","sale_price"]

