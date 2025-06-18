from django.shortcuts import render, redirect, HttpResponse
from .models import Site, Customer, Worksheet, Service, Stock
from .forms import SiteForm, StockForm, CustomerForm, WorksheetForm, ServiceForm

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, from workforms</h1>")

                # Sites Views #
                ###############
def sites(request):
    sites = Site.objects.all()
    return render(request, 'sites.html', {'sites': sites})

def add_site(request):
    if request.method =="POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sites')
    else:
        form = SiteForm()
        return render(request, "add_site.html",{'form': form})
    
def edit_site(request, id):
    site = Site.objects.get(id=id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('/sites', site.id)
    else:
        form = SiteForm(instance=site)
    return render(request, 'edit_site.html', {'form': form})


                # Customer Views #
                ##################
def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})

def add_customer(request):
    if request.method =="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer')
    else:
        form = CustomerForm()
        return render(request, "add_customer.html",{'form': form})
    
def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/customer', customer.id)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'edit_customer.html', {'form': form})



                # Worksheet Views #
                ###################
def worksheet(request):
    worksheets = Worksheet.objects.all()
    return render(request, 'worksheet.html', {'worksheets': worksheets})

def add_worksheet(request):
    if request.method =="POST":
        form = WorksheetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/worksheet')
    else:
        form = WorksheetForm()
        return render(request, "add_worksheet.html",{'form': form})

def edit_worksheet(request, id):
    worksheet = Worksheet.objects.get(id=id)
    if request.method == 'POST':
        form = WorksheetForm(request.POST, instance=worksheet)
        if form.is_valid():
            form.save()
            return redirect('/worksheet', worksheet.id)
    else:
        form = WorksheetForm(instance=worksheet)
    return render(request, 'edit_worksheet.html', {'form': form})
    


                # Service Views #
                #################
def service(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})

def add_service(request):
    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/service')
    else:
        form = ServiceForm()
        return render(request, "add_service.html",{'form': form})
    
def edit_service(request, id):
    service = Service.objects.get(id=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('/service', service.id)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'edit_service.html', {'form': form})


                # Stock Views #
                ###############
def stock(request):
    stocks = Stock.objects.all()
    return render(request, 'stock.html', {'stocks': stocks})

def add_stock(request):
    if request.method =="POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/stock')
    else:
        form = StockForm()
        return render(request, "add_stock.html",{'form': form})
    
def edit_stock(request, id):
    stock = Stock.objects.get(id=id)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('/stock', stock.id)
    else:
        form = StockForm(instance=stock)
    return render(request, 'edit_stock.html', {'form': form})