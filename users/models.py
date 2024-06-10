from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    username = None
    email = models.EmailField(null=False, blank=True, unique = True, verbose_name = "Email")
    phone = PhoneNumberField(null=False, blank=True, unique = True, verbose_name = "Номер телефону")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'Users'
        verbose_name =  'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.email