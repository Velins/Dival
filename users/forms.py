from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserLoginForm(AuthenticationForm):
    class Meta:
            model = User
            fields = ['username','password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
                "first_name",
                "last_name",
                "username",
                "phone",
                "email",
                "password1",
                "password2",)
        
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
