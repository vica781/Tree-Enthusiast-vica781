# Generated by Django 4.2.9 on 2024-03-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_identification', '0018_alter_profile_image_alter_tree_tree_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='use_cloudinary',
            field=models.BooleanField(default=True),
        ),
    ]
