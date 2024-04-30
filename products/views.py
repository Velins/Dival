from django.shortcuts import render, get_list_or_404,  get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from products.models import Material, Style, Color, Products, Category

def catalog(request, category_slug):

    if category_slug == 'all':
        product = Products.objects.all()    
        category_name = 'Всі товари'
        color_counts = Products.objects.values('color__name').annotate(total=Count('color'))
        material_counts = Products.objects.values('material__name').annotate(total=Count('material'))
        style_counts = Products.objects.values('style__name').annotate(total=Count('style'))
    else:
        category = get_object_or_404(Category, slug=category_slug)
        category_name = category.name  
        product = Products.objects.filter(category=category)
        color_counts = Products.objects.filter(category__slug=category_slug).values('color__name').annotate(total=Count('color'))
        material_counts = Products.objects.filter(category__slug=category_slug).values('material__name').annotate(total=Count('material'))
        style_counts = Products.objects.filter(category__slug=category_slug).values('style__name').annotate(total=Count('style'))
        
    page = request.GET.get('page', 1)
    sort_option = request.GET.get('sort_option', None)


    selected_colors = request.GET.getlist('color[]')
    selected_materials = request.GET.getlist('material[]')
    selected_styles = request.GET.getlist('style[]')


    if selected_colors :
        product = product.filter(color__in=selected_colors) 
        
    if selected_materials :
        product = product.filter(material__in=selected_materials)  

    if selected_styles :
        product = product.filter(style__in=selected_styles)  

    if sort_option == '1':
        product = product.order_by('price')  # Від дешевих до дорогих
    elif sort_option == '2':
        product = product.order_by('-price') # Від дорогих до дешевих
    elif sort_option == '3':
        product = product.order_by('name')  # За назвою

    paginator = Paginator(product, 6)
    current_page = paginator.page(int(page))

    color = Color.objects.all()  
    material = Material.objects.all()
    style = Style.objects.all()
     
    context ={
        'title' : 'DiVal - Каталог',
        'category_name': category_name,
        'products': current_page,
        'colors': color,
        'color_counts': color_counts,
        'material_counts': material_counts,
        'style_counts': style_counts,
        'materials': material,
        'styles': style,
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