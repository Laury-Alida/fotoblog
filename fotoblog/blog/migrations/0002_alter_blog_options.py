# Generated by Django 4.2.2 on 2023-06-08 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('change_blog_title', 'can change the title of a blog ')]},
        ),
    ]
