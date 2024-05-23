from django.contrib import admin

from django.contrib import admin
from main.models import CarouselImage

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['id','image', 'order']
    list_editable = ['order']
