# Generated by Django 3.2.20 on 2023-08-31 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='\\media\tree.jpg', upload_to='media'),
        ),
    ]
