from django.urls import path

from orders import views

app_name = 'orders'
 
urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
    path('checkout/<int:order_id>/', views.liqpay_checkout, name='liqpay_checkout'),
    path('callback/', views.liqpay_callback, name='liqpay_callback'),
]
