# Generated by Django 4.2.4 on 2023-11-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_informacionextrausuario_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='nombreHotel',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='ubicacionHotel',
            field=models.CharField(max_length=200),
        ),
    ]
