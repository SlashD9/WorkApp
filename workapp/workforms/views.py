from django.shortcuts import render, redirect, HttpResponse
from .forms import StockForm

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, from workforms</h1>")

def sites(request):
    return render(request, 'sites.html')

def customer(request):
    return render(request, 'customer.html')

def worksheet(request):
    return render(request, 'worksheet.html')

def service(request):
    return render(request, 'service.html')

def stock(request):
    return render(request, 'stock.html')

def add_stock(request):
    if request.method =="POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/stock')
    else:
        form = StockForm()
        return render(request, "add_stock.html",{'form': form})