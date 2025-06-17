from django.shortcuts import render, redirect, HttpResponse
from .models import Site, Customer, Worksheet, Service, Stock
from .forms import SiteForm, StockForm, CustomerForm, WorksheetForm, ServiceForm

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, from workforms</h1>")

def sites(request):
    sites = Site.objects.all()
    return render(request, 'sites.html', {'sites': sites})

def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})

def worksheet(request):
    worksheets = Worksheet.objects.all()
    return render(request, 'worksheet.html', {'worksheets': worksheets})

def service(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})

def stock(request):
    stocks = Stock.objects.all()
    return render(request, 'stock.html', {'stocks': stocks})

def add_site(request):
    if request.method =="POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sites')
    else:
        form = SiteForm()
        return render(request, "add_site.html",{'form': form})

def add_customer(request):
    if request.method =="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer')
    else:
        form = CustomerForm()
        return render(request, "add_customer.html",{'form': form})

def add_worksheet(request):
    if request.method =="POST":
        form = WorksheetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/worksheet')
    else:
        form = WorksheetForm()
        return render(request, "add_worksheet.html",{'form': form})

def add_service(request):
    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/service')
    else:
        form = ServiceForm()
        return render(request, "add_service.html",{'form': form})
    

def add_stock(request):
    if request.method =="POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/stock')
    else:
        form = StockForm()
        return render(request, "add_stock.html",{'form': form})