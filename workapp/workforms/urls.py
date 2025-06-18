from django.urls import path
from .views import home, sites, worksheet, service, customer, stock
from django.contrib import admin
from . import views

admin.site.site_header = 'Worksheets'                    # default: "Django Administration"
admin.site.index_title = 'Selection Area'                 # default: "Site administration"
admin.site.site_title = 'Worksheets' # default: "Django site admin"

app_name = 'posts'

urlpatterns = [
    path('', sites, name='Sites'),
    
    path('sites/', sites, name='Sites'),
    path('sites/add_site/', views.add_site, name="add_site"),
    path('sites/edit_site/<id>', views.edit_site, name="edit_site"),

    path('customer/', customer, name='Customer'),
    path('customer/add_customer/', views.add_customer, name="add_customer"),
    path('customer/edit_customer/<id>', views.edit_customer, name="edit_customer"),

    path('worksheet/', worksheet, name='Worksheet'),
    path('worksheet/add_worksheet/', views.add_worksheet, name="add_worksheet"),
    path('worksheet/edit_worksheet/<id>', views.edit_worksheet, name="edit_worksheet"),

    path('service/', service, name='Service Sheet'),
    path('service/add_service/', views.add_service, name="add_service"),
    path('service/edit_service/<id>', views.edit_service, name="edit_service"),

    path('stock/', stock, name='Stock Sheet'),
    path('stock/add_stock/', views.add_stock, name="add_stock"),
    path('stock/edit_stock/<id>', views.edit_stock, name="edit_stock"),
    
    
]

