from django import forms
from .models import Site, Customer, Worksheet, Service, Stock 


class SiteForm(forms.ModelForm):
    class Meta :
        model = Site
        fields = ["site_name","address","town","county","country","aircode"]



class StockForm(forms.ModelForm):
    class Meta :
        model = Stock
        fields = ["qty","item","description","location","cost_price","sale_price"]

