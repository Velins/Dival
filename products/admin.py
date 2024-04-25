from django.contrib import admin

from products.models import Category, Products, Material, Style, Color

#admin.site.register(Category)
#admin.site.register(Products)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
