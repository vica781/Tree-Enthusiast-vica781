# Generated by Django 4.2.9 on 2024-03-17 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree_identification', '0020_auto_20240314_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='use_cloudinary',
        ),
    ]
