# Generated by Django 4.2.4 on 2023-11-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_hotel_nombrehotel_alter_hotel_ubicacionhotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacionextrausuario',
            name='habitacion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]