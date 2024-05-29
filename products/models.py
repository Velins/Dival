from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_category_id(value):
    if not value.startswith('C_') or len(value) != 7 or not value[2:].isdigit():
        raise ValidationError(
            _('ID категорії повинно починатись з "C_" і мати 5 цифр після цього.'),
            params={'помилка - ': value},
        )
    
def validate_products_id(value):
    if not value.startswith('P_') or len(value) != 7 or not value[2:].isdigit():
        raise ValidationError(
            _('ID товару повинно починатись з "P_" і мати 5 цифр після цього.'),
            params={'помилка - ': value},
        )
    
class Color(models.Model):
    id = models.CharField(primary_key=True,max_length=20, unique=True, verbose_name='ID')
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'Сolor'
        verbose_name =  'Колір'
        verbose_name_plural = 'Кольори'

    def __str__(self):
        return self.name

class Material(models.Model):
    id = models.CharField(primary_key=True,max_length=20, unique=True, verbose_name='ID')
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'Material'
        verbose_name =  'Матеріал'
        verbose_name_plural = 'Матеріали'

    def __str__(self):
        return self.name

class Style(models.Model):
    id = models.CharField(primary_key=True,max_length=20, unique=True, verbose_name='ID')
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'Style'
        verbose_name =  'Стиль'
        verbose_name_plural = 'Стилі'

    def __str__(self):
        return self.name
    
class Category(models.Model):
    id = models.CharField(primary_key=True,max_length=7, unique=True, validators=[validate_category_id], verbose_name='ID')
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'Category'
        verbose_name =  'Категорія'
        verbose_name_plural = 'Категорії'
        
    def __str__(self):
        return self.name

class Products(models.Model):
    id = models.CharField(primary_key=True, max_length=7, unique=True, validators=[validate_products_id], verbose_name='ID')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категорія')
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE, verbose_name='Колір')
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE, verbose_name='Матеріал')
    style = models.ForeignKey(to=Style, on_delete=models.CASCADE, verbose_name='Стиль')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    image = models.ImageField(upload_to='products_images', blank=True, null=True, verbose_name='Зображення в розмірі 1920 X 1080')
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, verbose_name='Ціна')
    discount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, verbose_name='Знижка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')
    
    class Meta:
        db_table = 'Products'
        verbose_name =  'Товар'
        verbose_name_plural = 'Товари'
        ordering = ("id",)

    def __str__(self):
         return f'{self.name}, кількість - {self.quantity}'
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    
    def sell_price(self):
        if self.discount:
            return round (self.price - self.price * self.discount/100, 2)
        return self.price

