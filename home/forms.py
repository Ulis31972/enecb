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
        # widgets = {
        #     'condicion': forms.Textarea(attrs={'rows': 2}),
        # }
        
        widgets = {
            'condicion': forms.Textarea(attrs={'rows': 2}),
            'nombre': forms.TextInput(attrs={'required': 'required'}),
            'curp': forms.TextInput(attrs={'required': 'required'}),
        }

    def clean_imagen(self):
        # Verifica si se proporciona una nueva imagen antes de actualizarla
        imagen = self.cleaned_data.get('imagen')
        if not imagen:
            return None  # No se proporcionó una nueva imagen
        return imagen
    
    
class UsuariosFormPro(forms.ModelForm):
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
        fields = ['nombre', 'curp', 'telefonoEmergencia', 'condicion', 'informacionTec', 'tipoUsuario', 'hotel', 'habitacion', 'imagen']  # Excluye el campo 'id' del formulario
        labels = {
            'nombre': 'Nombre',
            'curp': 'CURP',
            'telefonoEmergencia': 'Teléfono de Emergencia',
            'condicion': 'Condición',
            'informacionTec': 'Tecnológico de Procedencia',
            'tipoUsuario': 'Tipo de Usuario',
            'hotel': 'Hotel',
            'habitacion': 'Habitación',
            'imagen': 'Actualizar Imagen',
        }
        # widgets = {
        #     'condicion': forms.Textarea(attrs={'rows': 2}),
        # }
        
        widgets = {
            'condicion': forms.Textarea(attrs={'rows': 2}),
            'informacionTec': forms.Select(attrs={"style":"width: 100%"}),
        }

    def clean_imagen(self):
        # Verifica si se proporciona una nueva imagen antes de actualizarla
        imagen = self.cleaned_data.get('imagen')
        if not imagen:
            return None  # No se proporcionó una nueva imagen
        return imagen