# Generated by Django 4.2.9 on 2024-03-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_identification', '0012_alter_tree_introduction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]