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
        fields = ["site_name","customer_name","customer_email","customer_phone"]

#Worksheet form
#Requires fields to be added
class WorksheetForm(forms.ModelForm):
    class Meta :
        model = Worksheet
        fields = ["site_name","date","start_time","end_time","travel_time","job_type","description","materials","num_electrcians","num_apprentices","electricians_name","customer_name","signature","image2","image3","image4","image5","image5","image6","status"]
    
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type':'time',
        }
        ))

    end_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            }
            ))
    
    date = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date', 
            }
        ))

#Service Form
#Requires fields to be added
class ServiceForm(forms.ModelForm):
    class Meta :
        model = Service
        fields = ["site_name","date","location","door_Code","installation_type","controller_type","controller_condition","selector_type","selector_other","door_type","door_condition","arm_type","arm_condition","roller_condition","battery_condition","internal_activation","internal_activation_condition","external_activation","external_activation_condition","safety_sensor","safety_sensor_condition","open_speed","close_speed","hold_open","hours","cycles","notes","image1","image2","image3","image4","image5","image6","status"]
        widgets = forms.TextInput(attrs={
            'class': 'form-control'
        }),
        intial='Name',

    date = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date', 
            }
        ))


class StockForm(forms.ModelForm):
    class Meta :
        model = Stock
        fields = ["qty","item","description","location","cost_price","sale_price"]

