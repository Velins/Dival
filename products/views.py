from django.shortcuts import render, get_list_or_404,  get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import QueryDict
from products.utils import q_search
from products.models import Material, Style, Color, Products, Category

def catalog(request, category_slug=None):
    selected_colors = request.GET.getlist('color[]')
    selected_materials = request.GET.getlist('material[]')
    selected_styles = request.GET.getlist('style[]')
    query = request.GET.get('q', None)

    if category_slug == 'all':
        product = Products.objects.all()
        category_name = 'Всі товари'
    elif query:
        product = q_search(query)
        category_name = 'Результати пошуку'
    else:
        category = get_object_or_404(Category, slug=category_slug)
        category_name = category.name
        product = Products.objects.filter(category=category)

    if selected_colors:
        product = product.filter(color__in=selected_colors)
    if selected_materials:
        product = product.filter(material__in=selected_materials)
    if selected_styles:
        product = product.filter(style__in=selected_styles)

    # Count available options for filters after applying the current filters
    color_counts = product.values('color__id', 'color__name').annotate(total=Count('color'))
    material_counts = product.values('material__id', 'material__name').annotate(total=Count('material'))
    style_counts = product.values('style__id', 'style__name').annotate(total=Count('style'))

    sort_option = request.GET.get('sort_option')
    if sort_option == '1':
        product = product.order_by('price')  # Від дешевих до дорогих
    elif sort_option == '2':
        product = product.order_by('-price')  # Від дорогих до дешевих
    elif sort_option == '3':
        product = product.order_by('name')  # За назвою

    paginator = Paginator(product, 8)
    page = request.GET.get('page', 1)
    current_page = paginator.page(int(page))

    color = Color.objects.all()
    material = Material.objects.all()
    style = Style.objects.all()

    query_params = QueryDict(mutable=True)
    query_params.setlist('color[]', selected_colors)
    query_params.setlist('material[]', selected_materials)
    query_params.setlist('style[]', selected_styles)
    if sort_option:
        query_params['sort_option'] = sort_option

    context = {
        'title': 'DiVal - Каталог',
        'category_name': category_name,
        'products': current_page,
        'colors': color,
        'color_counts': color_counts,
        'material_counts': material_counts,
        'style_counts': style_counts,
        'materials': material,
        'styles': style,
        'slug_url': category_slug,
        'selected_colors': selected_colors,
        'selected_materials': selected_materials,
        'selected_styles': selected_styles,
        'query_params': query_params.urlencode(),
    }
    return render(request, 'products/catalog.html', context)

def product(request, product_slug):

    product = Products.objects.get(slug = product_slug)

    context ={
        'title' : product.name,
        'product' : product
    }  
    
    return render(request,'products/product.html', context)