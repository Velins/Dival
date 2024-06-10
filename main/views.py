from django.shortcuts import render
import random
from products.models import Products
from main.models import CarouselImage

def index(request):
    
    product = Products.objects.filter(discount__gt=0)
    random_products = random.sample(list(product), min(4, len(product)))

    images = CarouselImage.objects.all()

    context ={
        'title' : 'DiVal - Головна сторінка',
        'products' : random_products,
        'images': images
    } 

    return render(request, 'main/index.html', context)

def about(request):

    context ={
        'title' : 'DiVal - Про нас'
    } 

    return render(request, 'main/about.html', context)

def payment_and_delivery(request):

    context ={
        'title' : 'DiVal - Оплата і доставка'
    } 

    return render(request, 'main/payment_and_delivery.html', context)

def cooperation(request):

    context ={
        'title' : 'DiVal - Умови співпраці'
    } 

    return render(request, 'main/cooperation.html', context)