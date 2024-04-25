from django.shortcuts import render

from products.models import Material, Style, Color

def catalog(request):

    color = Color.objects.all()

    context ={
        'title' : 'DiVal - Каталог',
        'products' :[
            {
                'image' : 'assets/img/products/shafa1.jpg',
                'name' : 'Шафа-купе MiroMark',
                'description' : 'Шафа-купе VIP-master з поличками та роздвіжними дверцятами',
                'price' : '5 300.00'
            },
            {
                'image' : 'assets/img/products/shafa2.jpg',
                'name' : 'Шафа-купе MiroMarkМВ2',
                'description' : 'Шафа-купе MiroMark 2-дверна з роздвіжними дверцятами',
                'price' : '4 330.00'
            },
            {
                'image' : 'assets/img/products/shafa3.jpg',
                'name' : 'Шафа-купе VMV',
                'description' : 'Шафа-купе VMV 2-дверна з великими роздвіжними дверцятами',
                'price' : '7 900.00'
            },
        ],
        'colors':color,
    } 
    return render(request,'products/catalog.html', context)

def product(request):
    context ={
        'title' : 'DiVal - Товар'
    } 
    return render(request,'products/product.html', context)