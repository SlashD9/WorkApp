from django import forms
from .models import Site, Customer, Worksheet, Service, Stock 


class SiteForm(forms.ModelForm):
    class Meta :
        model = Site
        fields = ["site_name","address","town","county","country","aircode"]

#Customer Form
#Requires fields to be added
class CustomerForm(forms.ModelForm):
    class Meta :
        model = Customer
        fields = ["site_name"]

#Worksheet form
#Requires fields to be added
class WorksheetForm(forms.ModelForm):
    class Meta :
        model = Worksheet
        fields = ["site_name"]

#Service Form
#Requires fields to be added
class ServiceForm(forms.ModelForm):
    class Meta :
        model = Service
        fields = ["site_name"]

class StockForm(forms.ModelForm):
    class Meta :
        model = Stock
        fields = ["qty","item","description","location","cost_price","sale_price"]

