from django.shortcuts import render

# Create your views here.
def home(request):
    data = dict()
    import datetime
    data['time'] = datetime.datetime.now()
    return render(request,"home.html",context=data)

def holdings(request):
    data = dict()
    return render(request,"holdings.html",context=data)

def add_currency(request):
    data = dict()
    return render(request,"add_currency.html",context=data)

def update_x_rates(request):
    data=dict()
    return render(request,"update_x_rates.html",context=data)