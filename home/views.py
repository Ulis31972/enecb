from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML,CSS
import weasyprint
from enecb import settings
import os
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def indexFormal(request):
    return render(request, 'indexFormal.html', {})

def horario(request):
    return render(request, 'horario.html',{})

@login_required(login_url='/login/')
def credencial(request, id):
    try:
        usuario = Usuarios.objects.get(id=id)
    except:
        usuario = None
    
    try:
        extraInfo = InformacionExtraUsuario.objects.get(user=request.user)
    except:
        extraInfo = None

    if request.method == "POST":
        weasyprint_settings = {
            'keep_image_data': True,  # Para incluir imágenes dentro del SVG
        }
        # Obtén la ruta al archivo CSS
        css_url = os.path.join(settings.BASE_DIR, 'home/static/css/credenciales/credencialfrentePDF.css')
        # Obtén la ruta al archivo de imagen
        image_url = extraInfo.imagen.path

        # Carga la plantilla HTML
        template = get_template("credenciales/credencialesFront.html")
        context = {"name": "CredencialFrente", "firstName": firstName, "lastName": lastName, "extraInfo": extraInfo}
        html_template = template.render(context)

        # Genera el PDF con WeasyPrint
        pdf = weasyprint.HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(
            stylesheets=[weasyprint.CSS(css_url)],
            weasyprint_settings = weasyprint_settings,
        )

        # Configura la respuesta HTTP y devuelve el PDF
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="archivo.pdf"'
        return response
    else:
        context = {
            "usuario":usuario, 
        }
        return render(request, 'credenciales/mostrarCredenciales.html', context)
    
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect the user to a page after login.
            return redirect('indexFormal')
        else:
            # Show an error message if authentication fails.
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'account/login.html', {})

@login_required(login_url='/login/')
def registroAsistencia(request, id):
    if request.user.has_perm('home.add_informacionextrausuario'):
        print("Tiene permisos")
    fecha_hora_local = timezone.now()
    
    # registro=RegistroAsistencia.objects.create(
    #     fechaRegistro = fecha_hora_local.strftime("%d/%m/%Y"),
    #     horaRegistro = fecha_hora_local.strftime("%H:%M"),
    #     user_id = id
    # )
    
    return render(request, 'registroAsistencia.html', {})

@login_required(login_url='/login/')
def perfil(request):
    user = request.user
    hasInfo = False
    if(request.method == "GET"):
        form = CambiarLogoForm()
        try:
            extraInfo = InformacionExtraUsuario.objects.get(user=user)
            hasInfo = True
        except:
            extraInfo = None
            hasInfo = False
        context={
            'user':user,
            'extraInfo':extraInfo,
            'hasInfo':hasInfo,
            'form':form
        }
        return render(request, 'perfil.html', context)
    else:
        try:
            extraInfo = InformacionExtraUsuario.objects.get(user=user)
            form = CambiarLogoForm(request.POST, request.FILES, instance=extraInfo)
            hasInfo = True
        except:
            extraInfo = None
            form = CambiarLogoForm(request.POST, request.FILES)
            hasInfo = False
        
        try:
            if form.is_valid():
                form.save()
            else:
                print("Formulario invalido")
        except:
            print("Error al guardar")

        return redirect('perfil')
    
@login_required(login_url='/login/')
def listaUsuariosTecnologicos(request):
    try:
        tecnologico = InformacionExtraUsuario.objects.get(user=request.user)
        usuarios = Usuarios.objects.filter(informacionTec=tecnologico).order_by('id')
    except:
        usuarios = None
    
    # if request.method == 'POST':
    #     form = UsuariosForm(request.POST, request.FILES, instance=usuario)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('detalle_usuario', id_usuario=id_usuario)
    else:
        form = UsuariosForm()

    return render(request, 'listaUsuariosTecnologicos.html', {
        'form': form,
        'usuarios':usuarios
        })

@login_required(login_url='/login/')
def actualizarUsuario(request, id):
    usuario = Usuarios.objects.get(id=id)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listaUsuariosTecnologicos')
        else:
            print("no es valido")
    else:
        return redirect('listaUsuariosTecnologicos')
    
# def registro(request):
#     if(request.method == "GET"):
#         try:
#             tecnologico_choices = [(t.pk, t.nombreTec) for t in Tecnologico.objects.all()]
#             form = UserRegistrationForm(tecnologico_choices=tecnologico_choices)
#         except:
#             form = UserRegistrationForm()
#         return render(request, 'account/register.html', {'form':form})
#     else:
#         try:
#             tecnologico_choices = [(t.pk, t.nombreTec) for t in Tecnologico.objects.all()]
#         except:
#             tecnologico_choices=None
#         form = UserRegistrationForm(request.POST, tecnologico_choices=tecnologico_choices)
#         print("entra post")
#         if form.is_valid():
#             print("Formulario valido")
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             modalidad = form.cleaned_data['modalidad']
#             tipo_usuario = form.cleaned_data['tipo_usuario']
#             tecOrigen = form.cleaned_data['tecnologico']
#             email = form.cleaned_data['email']
#             cellphone = form.cleaned_data['cellphone']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             try:
#                 user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
#                 user.save()
#                 extraInfo = InformacionExtraUsuario.objects.create(
#                     user=user,
#                     modalidad=modalidad,
#                     tipoUsuario=tipo_usuario,
#                     tecOrigen=Tecnologico.objects.get(pk=tecOrigen),
#                     hotel = Hotel.objects.get(nombreHotel="Hotel Villa Montaña"),
#                 )
#                 extraInfo.save()
#                 return redirect('indexFormal')
#             except:
#                 return redirect('registro')
#         else:
#             print("Formulario invalido")
#             return redirect('registro')
        

