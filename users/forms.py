from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

# views.py
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class UserLoginForm(AuthenticationForm):
    class Meta:
            model = User
            fields = ('email','password')

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
                "first_name",
                "last_name",
                "phone",
                "email",
                "password1",
                "password2",)
        
        first_name = forms.CharField()
        last_name = forms.CharField()
        phone = forms.CharField()
        email = forms.CharField()
        password1 = forms.CharField()
        password2 = forms.CharField()

class ProfileForm(UserChangeForm):
     class Meta:
        model = User
        fields = (
                "first_name",
                "last_name",
                "phone",
                "email",)
        
        first_name = forms.CharField()
        last_name = forms.CharField()
        phone = forms.CharField()
        email = forms.CharField()

class CustomPasswordChangeView(PasswordChangeView):

    success_url = reverse_lazy('user:profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Ваш пароль успішно змінено.')
        return super().form_valid(form)
