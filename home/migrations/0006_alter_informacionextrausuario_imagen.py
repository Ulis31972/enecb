# Generated by Django 4.2.4 on 2023-11-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_informacionextrausuario_habitacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacionextrausuario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/'),
        ),
    ]