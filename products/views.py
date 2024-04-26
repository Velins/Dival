from django.shortcuts import render

from products.models import Material, Style, Color, Products

def catalog(request):

    color = Color.objects.all()

    product = Products.objects.all()

    context ={
        'title' : 'DiVal - Каталог',
        'products': product,
        'colors':color,
    } 
    return render(request,'products/catalog.html', context)

def product(request):
    context ={
        'title' : 'DiVal - Товар'
    } 
    return render(request,'products/product.html', context)