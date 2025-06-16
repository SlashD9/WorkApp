from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, from workforms</h1>")

def customer_site(request):
    return HttpResponse("<h1>Customer Site</h1>")

def worksheet(request):
    return HttpResponse("<h1>Worksheet</h1>")

def service_sheet(request):
    return HttpResponse("<h1>Service Sheet</h1>")