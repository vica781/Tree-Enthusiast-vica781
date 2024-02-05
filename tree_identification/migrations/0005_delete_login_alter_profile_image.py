# Generated by Django 4.2.9 on 2024-01-31 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_identification', '0004_remove_profile_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]