# Generated by Django 5.0.2 on 2024-04-30 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=100, null=True),
        ),
    ]