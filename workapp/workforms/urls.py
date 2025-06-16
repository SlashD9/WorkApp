from django.urls import path
from .views import home, sites, worksheet, service, customer, stock
from django.contrib import admin
from . import views

admin.site.site_header = 'Worksheets'                    # default: "Django Administration"
admin.site.index_title = 'Selection Area'                 # default: "Site administration"
admin.site.site_title = 'Worksheets' # default: "Django site admin"

app_name = 'posts'

urlpatterns = [
    path('', home, name='home'),
    path('sites/', sites, name='Sites'),
    path('customer/', customer, name='Customer'),
    path('worksheet/', worksheet, name='Worksheet'),
    path('service/', service, name='Service Sheet'),
    path('stock/', stock, name='Stock Sheet'),
    path('stock/add_stock/', views.add_stock, name="add_stock"),
    
]

