from django.shortcuts import render
from myapp import support_functions
from myapp.models import Currency
# Create your views here.
def home(request):
    data = dict()
    import datetime
    data['time'] = datetime.datetime.now()
    return render(request,"home.html",context=data)

def maintenance(request):
    data = dict()
    try:
        form_submitted = request.GET['form_submitted']
        choice = request.GET['selection']
        print(choice)
        if choice == "currencies":
            support_functions.add_currencies(support_functions.get_currency_list())
    except:
        pass
    return render(request,"maintenance.html",context=data)

def view_currencies(request):
    data = dict()
    c_list = Currency.objects.all()
    data['currencies'] = c_list
    from bs4 import BeautifulSoup
    import requests
    page = requests.get("https://en.wikipedia.org/wiki/Main_Page")
    data['wiki_data'] = page.text

    return render(request,'currencies.html',context=data)


def holdings(request):
    data = dict()
    return render(request,"holdings.html",context=data)

def add_currency(request):
    data = dict()
    return render(request,"add_currency.html",context=data)

def update_x_rates(request):
    data=dict()
    return render(request,"update_x_rates.html",context=data)

