from django.shortcuts import render, get_list_or_404,  get_object_or_404
from django.core.paginator import Paginator
from products.models import Material, Style, Color, Products, Category

def catalog(request, category_slug, page=1):

    if category_slug == 'all':
        product = Products.objects.all()
        category_name = "Всі товари"
    else:
        product = get_list_or_404(Products.objects.filter(category__slug = category_slug))
        category = get_object_or_404(Category, slug=category_slug)
        category_name = category.name  

    paginator = Paginator(product, 2)
    current_page = paginator.page(page)

    color = Color.objects.all()  
    
    context ={
        'title' : 'DiVal - Каталог',
        'category_name': category_name,
        'products': current_page,
        'colors': color,
        'slug_url': category_slug
    } 
    return render(request,'products/catalog.html', context)

def product(request, product_slug):

    product = Products.objects.get(slug = product_slug)

    context ={
        'title' : 'DiVal - Товар',
        'product' : product
    }  
    
    return render(request,'products/product.html', context)