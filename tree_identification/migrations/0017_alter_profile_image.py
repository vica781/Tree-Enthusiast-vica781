# Generated by Django 4.2.9 on 2024-03-09 09:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree_identification', '0016_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default', max_length=255, verbose_name='image'),
        ),
    ]
