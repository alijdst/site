# Generated by Django 3.2.20 on 2023-09-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_delete_custommanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
