from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import auth, messages
from django.shortcuts import redirect
from carts.utils import get_user_carts
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Prefetch
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from carts.models import Cart
from orders.models import Order, OrderItem
from django.urls import resolve

def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, "Ви увійшли в аккаунт!")
                
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, "Неправильний email або пароль!")
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = UserLoginForm()

    context = {
        'title': 'Логін',
        'form': form,
    }

    return render(request,'users/login.html', context) 


def registration (request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
                form.save() 

                session_key = request.session.session_key
                
                user = form.instance
                auth.login(request, user)

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                messages.success(request, "Ви успішно зареєстувались !")
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserRegistrationForm()

    if request.path == 'user/login/':
        is_login_page = True
    else:
        is_login_page = False
    
    context = {
        'title' : 'Реєстрація',
        'form' : form,
        'is_login_page' : is_login_page
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

def users_carts(request):
    context = {
        'title' : 'Кошик'
    }
    return render(request, "users/users_cart.html", context)

@login_required
def orders (request):
    orders = Order.objects.filter(user=request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            ).order_by("-id")
    
    form = ProfileForm(instance = request.user)
    
    context = {
        'title' : 'Мої замовлення',
        'form' : form,
        'orders': orders,
    }

    return render(request,'users/orders.html', context) 


@login_required
def logout (request):
    auth.logout(request)
    return redirect(reverse('main:index'))

