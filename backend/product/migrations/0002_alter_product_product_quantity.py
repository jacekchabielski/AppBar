# Generated by Django 4.1.2 on 2022-11-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
