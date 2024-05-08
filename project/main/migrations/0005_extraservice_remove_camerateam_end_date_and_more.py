# Generated by Django 5.0.2 on 2024-05-03 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tag_alter_product_image1_alter_product_image2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reduction', models.DecimalField(decimal_places=2, max_digits=10)),
                ('banner', models.ImageField(upload_to='extraService/')),
            ],
        ),
        migrations.RemoveField(
            model_name='camerateam',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='camerateam',
            name='salle',
        ),
        migrations.RemoveField(
            model_name='camerateam',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='camerateam',
            name='user',
        ),
        migrations.AddField(
            model_name='reservation',
            name='photograph',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.camerateam'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='salle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.salle'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='extra_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.extraservice'),
        ),
    ]