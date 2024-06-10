# Generated by Django 4.2.11 on 2024-06-08 14:52

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(max_length=7, primary_key=True, serialize=False, unique=True, validators=[products.models.validate_category_id], verbose_name='ID'),
        ),
    ]
