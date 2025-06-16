from django.urls import path
from .views import home, worksheet, service_sheet, customer_site
from django.contrib import admin

admin.site.site_header = 'Worksheets'                    # default: "Django Administration"
admin.site.index_title = 'Selection Area'                 # default: "Site administration"
admin.site.site_title = 'Worksheets' # default: "Django site admin"

urlpatterns = [
    path('', home, name='home'),
    path('sites/', customer_site, name='Customer Sites'),
    path('worksheet/', worksheet, name='Worksheet'),
    path('service/', service_sheet, name='Service Sheet'),
    
]

