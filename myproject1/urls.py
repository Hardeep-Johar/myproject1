"""myproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name ="home"),
    path('home',views.home, name='home'),
    path('maintenance', views.maintenance, name='maintenance'),
    path('currencies',views.view_currencies, name='currencies'),
    path('currency-selection', views.currency_selection, name="currency_selector"),
    path('exchange_rate_info',views.exch_rate,name="exchange_rate_info"),
    path('map',views.map,name="map"),
    path('register',views.register_new_user,name="register_user"),
    path('new-currency',views.add_currency, name="add_currency"),
    path('view-holdings', views.holdings, name="holdings"),
    path('update-x-rates', views.update_x_rates, name="update"),

]