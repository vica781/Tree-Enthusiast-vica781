# Generated by Django 4.2.9 on 2024-02-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_identification', '0009_tree'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tree',
            old_name='image',
            new_name='tree_image',
        ),
        migrations.RemoveField(
            model_name='tree',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tree',
            name='title',
        ),
        migrations.AddField(
            model_name='tree',
            name='common_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tree',
            name='introduction',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tree',
            name='origin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tree',
            name='tree_habitat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tree',
            name='tree_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
