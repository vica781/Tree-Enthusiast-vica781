# Generated by Django 4.2.9 on 2024-02-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_identification', '0010_rename_image_tree_tree_image_remove_tree_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='introduction',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='tree',
            name='tree_habitat',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
