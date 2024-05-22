from django.contrib import admin
from django.urls import path

from users import views

app_name = 'users'
 
urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('users-cart/', views.users_carts, name='user_cart'),
    path('orders/', views.orders, name='orders'),
    path('logout/', views.logout, name='logout'),
]
