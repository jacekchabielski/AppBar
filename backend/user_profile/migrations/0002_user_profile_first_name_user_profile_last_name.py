# Generated by Django 4.1.2 on 2023-01-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]