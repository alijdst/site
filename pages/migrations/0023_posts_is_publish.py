# Generated by Django 3.2.20 on 2023-09-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_alter_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
    ]
