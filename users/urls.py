from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from users import views
from users.forms import CustomPasswordChangeView

app_name = 'users'
 
urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('users-cart/', views.users_carts, name='user_cart'),
    path('orders/', views.orders, name='orders'),
    path('logout/', views.logout, name='logout'),

    path('password-change/',  CustomPasswordChangeView.as_view(template_name='users/password_change.html'), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name="password_change_done"),
]
