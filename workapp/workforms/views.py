from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .models import Site, Customer, Worksheet, Service, Stock
from .forms import SiteForm, StockForm, CustomerForm, WorksheetForm, ServiceForm



def dashboard(request):
    if request.user.is_authenticated:
        return redirect('next')
    else:
        return HttpResponse(f"Please log in to acces this page.")
    
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, from workforms</h1>")

                # Sites Views #
                ###############
@login_required
def sites(request):
    sites = Site.objects.all()
    return render(request, 'sites.html', {'sites': sites})

@login_required
def add_site(request):
    if request.method =="POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sites')
    elif "delete" in request.POST:
        pk = request.Post.get("delete")
        site = Site.objects.get(id=pk)
        site.delete
    else:
        form = SiteForm()
        return render(request, "add_site.html",{'form': form})
    
@login_required
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

@login_required
def delete_site(request, id):
    site = Site.objects.get(id=id)
    site.delete()
    return redirect("/site/")



                # Customer Views #
                ##################
@login_required
def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})

@login_required
def add_customer(request):
    if request.method =="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer')
    else:
        form = CustomerForm()
        return render(request, "add_customer.html",{'form': form})

@login_required
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

@login_required
def delete_customer(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('/customer')



                # Worksheet Views #
                ###################
@login_required
def worksheet(request):
    worksheets = Worksheet.objects.all()
    return render(request, 'worksheet.html', {'worksheets': worksheets})

@login_required
def add_worksheet(request):
    if request.method =="POST":
        form = WorksheetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/worksheet')
    else:
        form = WorksheetForm()
        return render(request, "add_worksheet.html",{'form': form})

@login_required
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

@login_required
def delete_worksheet(request, id):
    worksheet = Worksheet.objects.get(id=id)
    worksheet.delete()
    return redirect('/worksheet')
    


                # Service Views #
                #################
@login_required
def service(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})

@login_required
def add_service(request):
    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/service')
    else:
        form = ServiceForm()
        return render(request, "add_service.html",{'form': form})
    
@login_required
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

@login_required
def delete_service(request, id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect('/service')


                # Stock Views #
                ###############
@login_required
def stock(request):
    stocks = Stock.objects.all()
    return render(request, 'stock.html', {'stocks': stocks})

@login_required
def add_stock(request):
    if request.method =="POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/stock')
    else:
        form = StockForm()
        return render(request, "add_stock.html",{'form': form})
    
@login_required
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

@login_required
def delete_stock(request, id):
    stock = Stock.objects.get(id=id)
    stock.delete()
    return redirect('/stock')