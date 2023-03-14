# Generated by Django 4.1.2 on 2023-03-14 15:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_alter_recipeproduct_options'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='order.order')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_idd', to='recipe.recipe')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
