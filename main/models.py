from django.db import models

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel', verbose_name="Зображення")
    order = models.PositiveIntegerField(default=0, verbose_name="Номер в черзі ")

    class Meta:
        ordering = ['order']
        verbose_name =  'Зображення для каруселі'
        verbose_name_plural = 'Зображення для каруселі'

    def __str__(self):
        return f"Зображення №{self.id}"
