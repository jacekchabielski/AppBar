# Generated by Django 4.1.2 on 2022-12-01 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_category', '0002_recipe_category_image_recipe_category_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe_category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='recipe_category',
            name='thumbnail',
        ),
    ]
