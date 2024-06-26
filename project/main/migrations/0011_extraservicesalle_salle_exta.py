# Generated by Django 5.0.2 on 2024-05-08 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_salle_facebook_alter_salle_image2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraServiceSalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='salle',
            name='Exta',
            field=models.ManyToManyField(blank=True, to='main.extraservicesalle'),
        ),
    ]
