from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.customers_list),
    path('/<pk>', views.customers_detail),
]
