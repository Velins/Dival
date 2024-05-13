from django.contrib import admin

from products.models import Category, Products, Material, Style, Color

#admin.site.register(Category)
#admin.site.register(Products)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['quantity', 'price', 'discount']
    search_fields = ['name', 'quantity', 'price', 'discount', 'description']
    list_filter = ['quantity', 'discount', 'category', 'color', 'material', 'style']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
