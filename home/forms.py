from django import forms
from .models import *
class CambiarLogoForm(forms.ModelForm):
    class Meta:
        model = InformacionExtraUsuario
        fields = ['logo']
        
        
class UsuariosForm(forms.ModelForm):
    # Limita las opciones del campo tipoUsuario
    # TIPOS_USUARIO_CHOICES = [
    #     ("Visitante", "Visitante"),
    #     ("Asesor", "Asesor"),
    #     ("Participante Ciencias Básicas", "Participante Ciencias Básicas"),
    #     ("Participante Económico Administrativo", "Participante Económico Administrativo"),
    # ]

    # tipoUsuario = forms.ChoiceField(choices=TIPOS_USUARIO_CHOICES)

    class Meta:
        model = Usuarios
        exclude = ['id', 'informacionTec', 'tipoUsuario', 'hotel', 'habitacion']  # Excluye el campo 'id' del formulario
        labels = {
            'nombre': 'Nombre',
            'curp': 'CURP',
            'telefonoEmergencia': 'Teléfono de Emergencia',
            'condicion': 'Condición',
            # 'informacionTec': 'Tecnológico de Procedencia',
            # 'tipoUsuario': 'Tipo de Usuario',
            # 'hotel': 'Hotel',
            # 'habitacion': 'Habitación',
            'imagen': 'Actualizar Imagen',
        }
        widgets = {
            'condicion': forms.Textarea(attrs={'rows': 2}),
        }

    def clean_imagen(self):
        # Verifica si se proporciona una nueva imagen antes de actualizarla
        imagen = self.cleaned_data.get('imagen')
        if not imagen:
            return None  # No se proporcionó una nueva imagen
        return imagen



# class UserRegistrationForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=100,
#         label='Nombre',
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     last_name = forms.CharField(
#         max_length=100,
#         label='Apellidos',
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     username = forms.CharField(
#         max_length=50,
#         label='Nombre de Usuario',
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     email = forms.EmailField(
#         label='Correo Electronico',
#         widget=forms.EmailInput(attrs={'class': 'form-control'})
#     )
#     cellphone = forms.CharField(
#         label="Telefono Celular",
#         max_length=10,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         label='Contraseña'
#     )
#     modalidad = forms.ChoiceField(
#         choices=[
#             ('Presencial', 'Presencial'),
#             ('Virtual', 'Virtual'),
#         ],
#         label='Modalidad',
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
#     tipo_usuario = forms.ChoiceField(
#         choices=[
#             ('Organizadores', 'Organizadores'),
#             ('Ciencias Básicas', 'Ciencias Básicas'),
#             ('Autoridad', 'Autoridad'),
#             ('Visitante', 'Visitante'),
#         ],
#         label='Tipo de Usuario',
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
    
#     def __init__(self, *args, tecnologico_choices=None, **kwargs):
#         super(UserRegistrationForm, self).__init__(*args, **kwargs)
#         if tecnologico_choices:
#             self.fields['tecnologico'] = forms.ChoiceField(
#                 choices=tecnologico_choices,
#                 label='Tecnologico de Procedencia',
#                 widget=forms.Select(attrs={'class': 'form-control'})
#             )
