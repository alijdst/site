# Generated by Django 3.2.20 on 2023-08-31 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_posts_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-created', '-updated'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
