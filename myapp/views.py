from django.shortcuts import render
from myapp import support_functions
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



def holdings(request):
    data = dict()
    return render(request,"holdings.html",context=data)

def add_currency(request):
    data = dict()
    return render(request,"add_currency.html",context=data)

def update_x_rates(request):
    data=dict()
    return render(request,"update_x_rates.html",context=data)

