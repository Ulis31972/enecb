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
    lastName= request.user.last_name
    extraInfo = InformacionExtraUsuario.objects.get(user=request.user)
    # print(extraInfo.tecOrigen.nombreTec)
    #Imprimir la credencial
    if request.method == "POST":
        template = get_template("credenciales/credencialesFront.html")
        context = {"name":"CredencialFrente","firstName":firstName,"lastName":lastName,"extraInfo":extraInfo}
        css_url = os.path.join(settings.BASE_DIR,'home\static\css\credenciales\credencialfrente.css')
        googleFonts= "https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible&family=Gothic+A1&family=KoHo&display=swap"
        print(css_url)
        html_template = template.render(context)
        html = HTML(string=html_template,base_url=request.build_absolute_uri())
        #pdf = html.write_pdf(stylesheets=[css_url],target="Prueba.pdf",presentational_hints=True)
        pdf = weasyprint.HTML(string=html_template).write_pdf()
        response = HttpResponse(pdf,content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="archivo.pdf"'
        #return render(request, 'credenciales/mostrarCredenciales.html')
        return response
    #Renderizar credencial
    else:
        context ={"firstName":firstName,"lastName":lastName,"extraInfo":extraInfo}
        return render(request, 'credenciales/mostrarCredenciales.html',context=context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect the user to a page after login.
            return redirect('index')
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