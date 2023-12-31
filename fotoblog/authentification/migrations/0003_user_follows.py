# Generated by Django 4.2.2 on 2023-06-08 10:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0002_auto_20230608_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(limit_choices_to={'role': 'CREATOR'}, to=settings.AUTH_USER_MODEL),
        ),
    ]
