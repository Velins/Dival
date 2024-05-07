from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm
# Create your views here.

# Ваші імпорти та інші в'юшки

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Login',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration (request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
                form.save() 
                user = form.instance
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title' : 'DiVal - Реєстрація',
        'form' : form
    }
    return render(request,'users/registration.html', context)

def profile (request):
    context = {
        'title' : 'DiVal - Кабінет'
    }
    return render(request,'users/profile.html', context)   

def logout (request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))