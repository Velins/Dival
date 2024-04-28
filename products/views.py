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

def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context ={
        'title' : 'DiVal - Товар',
        'product' : product
    }  
    
    return render(request,'products/product.html', context=context)