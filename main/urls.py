from django.contrib import admin
from django.urls import path

from main import views

app_name = 'main'
 
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('payment-and-delivery/', views.payment_and_delivery, name='payment_and_delivery'),
    path('cooperation/', views.cooperation, name='cooperation'),
]
