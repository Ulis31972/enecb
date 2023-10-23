from django.db import models
from django.contrib.auth.models import User
# Create your models here.

HABITACIONES = [
            ('Individual', 'Individual'),
            ('Doble', 'Doble'),
            ('Triple', 'Triple')
        ]

UBICACIONES = [
    ('Edificio A','A'),
    ('Edificio B','B'),
    ('Edificio C','C'),
]
class Hotel(models.Model):
    nombreHotel = models.CharField(max_length=25,null=False)
    ubicacionHotel = models.CharField(max_length=45, null=False)

class ComplementoUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    fotoPerfil = models.CharField(max_length=100,null=False)
    tecOrigen = models.CharField(max_length=50, null=False)
    hospedaje = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class Precios(models.Model):
    tipoHabitacion = models.CharField(max_length=15,choices = HABITACIONES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

class Actividad(models.Model):
    nombreActividad = models.CharField(max_length=25, null=False)
    fechaActividad = models.DateTimeField(auto_now=False, auto_now_add=False,null=False)
    ubicacionActividad = models.CharField(max_length=10)
    responsableActividad = models.CharField(max_length=50) #Este se puede sustituir por un FK si el Staff tambien contara con acceso al sistema
# precios (tipo (opciones individual, doble, triple), precio, hotel (foreign))
    
class RegistroAsistencia(models.Model):
    # actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fechaRegistro = models.DateTimeField()
    horaRegistro = models.TimeField()
    # ubicacionRegistro = models.CharField(max_length=10)
    # responsableRegistro = models.CharField(max_length=50)
    
class Tecnologico(models.Model):
    nombreTec = models.CharField(max_length=50, null=False)
    logo = models.ImageField(upload_to='logos/')
    
class InformacionExtraUsuario(models.Model):
    MODALIDAD_CHOICES = (
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
    )
    cargo = models.CharField(max_length=50, null=False)
    tecOrigen = models.ForeignKey(Tecnologico, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    modalidad = models.CharField(max_length=50, null=False, choices=MODALIDAD_CHOICES)
    imagen = models.ImageField(upload_to='fotos/')
    tipoUsuario = models.CharField(null=False, max_length=20, default="Visitante") 