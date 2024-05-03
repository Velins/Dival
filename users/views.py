from django.shortcuts import render

# Create your views here.

def login (request):
    context = {
        'title' : 'DiVal - Авторизація'
    }
    return render(request,'users/login.html', context)

def registration (request):
    context = {
        'title' : 'DiVal - Реєстрація'
    }
    return render(request,'users/registration.html', context)

def profile (request):
    context = {
        'title' : 'DiVal - Кабінет'
    }
    return render(request,'users/profile.html', context)   

def logout (request):
    ...