# Generated by Django 3.2.20 on 2023-08-31 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20230831_1950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-updated'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
