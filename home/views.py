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


from .models import RegistroAsistencia,InformacionExtraUsuario,Tecnologico


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def indexFormal(request):
    return render(request, 'indexFormal.html', {})

@login_required(login_url='/login/')
def credencial(request):
    firstName = request.user.first_name
    lastName = request.user.last_name
    extraInfo = InformacionExtraUsuario.objects.get(user=request.user)

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
        context = {"firstName": firstName, "lastName": lastName, "extraInfo": extraInfo}
        return render(request, 'credenciales/mostrarCredenciales.html', context=context)
    
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