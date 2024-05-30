from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
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

    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                                      email_template_name = 'users/password_reset_email.html',
                                                      success_url = reverse_lazy("users:password_reset_done")
                                                      ), name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                                                     success_url=reverse_lazy("users:password_reset_complete")), name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
