# Generated by Django 5.1.3 on 2024-12-04 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0007_imagemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemodel',
            old_name='price',
            new_name='name',
        ),
    ]