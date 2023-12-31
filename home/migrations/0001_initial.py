# Generated by Django 4.2.4 on 2023-11-07 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreActividad', models.CharField(max_length=25)),
                ('fechaActividad', models.DateTimeField()),
                ('ubicacionActividad', models.CharField(max_length=10)),
                ('responsableActividad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreHotel', models.CharField(max_length=25)),
                ('ubicacionHotel', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTec', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAsistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateTimeField()),
                ('horaRegistro', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Precios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoHabitacion', models.CharField(choices=[('Individual', 'Individual'), ('Doble', 'Doble'), ('Triple', 'Triple')], max_length=15)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='InformacionExtraUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=50)),
                ('modalidad', models.CharField(choices=[('Presencial', 'Presencial'), ('Virtual', 'Virtual')], max_length=50)),
                ('imagen', models.ImageField(blank=True, default='user.jpg', null=True, upload_to='fotos/')),
                ('tipoUsuario', models.CharField(default='Visitante', max_length=20)),
                ('habitacion', models.CharField(max_length=100)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.hotel')),
                ('tecOrigen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tecnologico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
