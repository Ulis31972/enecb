from django.db import models
from django.contrib.auth.models import User

# Create your models here.

HABITACIONES = [("Individual", "Individual"), ("Doble", "Doble"), ("Triple", "Triple")]

UBICACIONES = [
    ("Edificio A", "A"),
    ("Edificio B", "B"),
    ("Edificio C", "C"),
]

EVENTOS = [
    ("Ciencias básica", "Ciencias básica"),
    ("Economico Administrativas", "Economico Administrativas"),
]


class Hotel(models.Model):
    nombreHotel = models.CharField(max_length=100, null=False)
    ubicacionHotel = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.nombreHotel


class Precios(models.Model):
    tipoHabitacion = models.CharField(max_length=15, choices=HABITACIONES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class Actividad(models.Model):
    nombreActividad = models.CharField(max_length=25, null=False)
    fechaActividad = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=False
    )
    ubicacionActividad = models.CharField(max_length=10)
    responsableActividad = models.CharField(
        max_length=50
    )  # Este se puede sustituir por un FK si el Staff tambien contara con acceso al sistema


# precios (tipo (opciones individual, doble, triple), precio, hotel (foreign))


class RegistroAsistencia(models.Model):
    # actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fechaRegistro = models.DateTimeField()
    horaRegistro = models.TimeField()
    # ubicacionRegistro = models.CharField(max_length=10)
    # responsableRegistro = models.CharField(max_length=50)


# class Tecnologico(models.Model):
#     nombreTec = models.CharField(max_length=100, null=False)
#     logo = models.ImageField(upload_to="logos/", blank=True, null=True)


# class InformacionExtraUsuario(models.Model):
#     MODALIDAD_CHOICES = (
#         ("Presencial", "Presencial"),
#         ("Virtual", "Virtual"),
#     )
#     cargo = models.CharField(max_length=50, null=False)
#     tecOrigen = models.ForeignKey(Tecnologico, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     modalidad = models.CharField(max_length=50, null=False, choices=MODALIDAD_CHOICES)
#     imagen = models.ImageField(
#         upload_to="fotos/", null=True, blank=True, default="user.jpg"
#     )
#     tipoUsuario = models.CharField(null=False, max_length=20, default="Visitante")
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     habitacion = models.CharField(max_length=100, blank=True, null=True)
#     evento = models.CharField(max_length=100, choices=EVENTOS, null=True)

class InformacionExtraUsuario(models.Model):
    logo = models.ImageField(upload_to="logos/", blank=True, null=True, default="defaultLogo.png")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name


class Usuarios(models.Model):
    TIPOSUSUARIO = (
        ("Visitante", "Visitante"),
        ("Organizador", "Organizador"),
        ("Autoridad", "Autoridad"),
        ("Asesor", "Asesor"),
        ("Participante Ciencias Básicas", "Participante Ciencias Básicass"),
        ("Participante Económico Administrativo", "Participante Económico Administrativo")
    )

    nombre = models.CharField(max_length=200, null=False)
    curp = models.CharField(max_length=20, null=False)
    telefonoEmergencia = models.CharField(max_length=15, blank=True, null=True)
    condicion = models.TextField(blank=True, null=True)
    informacionTec= models.ForeignKey(InformacionExtraUsuario, on_delete=models.CASCADE)
    tipoUsuario = models.CharField(null=False, max_length=100, default="Visitante", choices=TIPOSUSUARIO)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    habitacion = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to="fotos/", null=True, blank=True, default="user.jpg")
    
    # Avientate unas migraciones, voy a desayunar en fa y regreso, checa que todo jale bien
    # ok