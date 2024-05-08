from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import auth, messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
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
                messages.success(request, "Ви увійшли в аккаунт!")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Логін',
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
                messages.success(request, "Ви успішно зареєстувались !")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title' : 'Реєстрація',
        'form' : form
    }
    return render(request,'users/registration.html', context)

@login_required
def profile (request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance = request.user)
        if form.is_valid():
                form.save()
                messages.success(request, "Персональні дані збережено !") 
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance = request.user)

    context = {
        'title' : 'Особистий кабінет',
        'form' : form
    }
    return render(request,'users/profile.html', context)   

@login_required
def logout (request):
    auth.logout(request)
    messages.success(request, "Ви вийшли з аккаунту!") 
    return redirect(reverse('main:index'))