# Generated by Django 5.0.2 on 2024-04-30 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
