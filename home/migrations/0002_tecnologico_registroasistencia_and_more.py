# Generated by Django 4.2.4 on 2023-10-08 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
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
            name='InformacionExtraUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=50)),
                ('modalidad', models.CharField(choices=[('Presencial', 'Presencial'), ('Virtual', 'Virtual')], max_length=50)),
                ('imagen', models.ImageField(upload_to='fotos/')),
                ('tecOrigen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tecnologico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]