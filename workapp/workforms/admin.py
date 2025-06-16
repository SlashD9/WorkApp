from django.contrib import admin



# Register your models here.
from workforms.models import Site, Customer, Pricing, Worksheet, Service, Stock


class SiteAdmin(admin.ModelAdmin):
    list_display = ["site_name", "address", "town", "county", "country", "aircode"]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["site_name", "customer_name"]
    list_display_links =["site_name", "customer_name"]

class CustomerPriceingAdmin(admin.ModelAdmin):
    list_display = ["site_name", "call_out_charge", "per_hour_charge", "service_charge"]

#class ChoicesAdmin(admin.ModelAdmin):
#    pass

class WorksheetAdmin(admin.ModelAdmin):
    list_display = ["site_name", "date", "status"]
    list_display_links =["site_name", "date", "status"]

class ServiceAdmin(admin.ModelAdmin):
    list_display = ["site_name", "date", "door_Code", "status"]
    list_display_links =["site_name", "date", "status"]

class StockAdmin(admin.ModelAdmin):
    list_display = ["location", "qty", "item", "description"]
    list_display_links = ["qty", "item"]


# Ordering Models as listed and not by alphabetical order
def get_app_list(self, request, app_label=None):
    """Return the installed apps that have been registered in admin.py"""
    app_dict = self._build_app_dict(request, app_label)
    app_list = list(app_dict.values())
    return app_list


admin.site.register(Site, SiteAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Pricing, CustomerPriceingAdmin)
#admin.site.register(Choices, ChoicesAdmin)
admin.site.register(Worksheet, WorksheetAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Stock, StockAdmin)
admin.AdminSite.get_app_list = get_app_list
