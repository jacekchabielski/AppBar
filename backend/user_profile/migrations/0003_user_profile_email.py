# Generated by Django 4.1.2 on 2023-01-19 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_user_profile_first_name_user_profile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
