from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')

    class Meta:
        db_table = 'Users'
        verbose_name =  'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.username