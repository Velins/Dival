from django.http import HttpResponse
from django.shortcuts import render

from products.models import Category

# Create your views here.
def index(request):

    context ={
        'title' : 'DiVal - Головна с    торінка',
    } 
    return render(request, 'main/index.html', context)

def about(request):
    context ={
        'title' : 'DiVal - Про нас'
    } 
    return render(request, 'main/about.html', context)