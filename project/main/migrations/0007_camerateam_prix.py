# Generated by Django 5.0.2 on 2024-05-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_camerateam_description_extraservice_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='camerateam',
            name='prix',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]