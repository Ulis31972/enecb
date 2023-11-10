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
def credencial(request):
    firstName = request.user.first_name
    lastName = request.user.last_name
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

@login_required(login_url='/login/')
def perfil(request):
    user = request.user
    hasInfo = False
    if(request.method == "GET"):
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
        }
        return render(request, 'perfil.html', context)
    else:
        return render(request, 'perfil.html', {})
    
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
        

def kln(request, algo):
    if (algo == "KLN"):
        users_data = [
            {'username': 'itcelaya', 'email': 'itcelaya@example.com', 'password': 'celaya2023', 'first_name': 'Instituto Tecnológico de Celaya'},
            {'username': 'itmorelia', 'email': 'itmorelia@example.com', 'password': 'morelia2023', 'first_name': 'Instituto Tecnológico de Morelia'},
            {'username': 'ittepic', 'email': 'ittepic@example.com', 'password': 'tepic2023', 'first_name': 'Instituto Tecnológico de Tepic'},
            {'username': 'itmerida', 'email': 'itmerida@example.com', 'password': 'merida2023', 'first_name': 'Instituto Tecnológico de Mérida'},
            {'username': 'itnuevolaredo', 'email': 'itnuevolaredo@example.com', 'password': 'nuevolaredo2023', 'first_name': 'Instituto Tecnológico de Nuevo Laredo'},
            {'username': 'itspurisima', 'email': 'itspurisima@example.com', 'password': 'purisima2023', 'first_name': 'Instituto Tecnológico Superior de Purísima del Rincón'},
            {'username': 'itsguanajuato', 'email': 'itsguanajuato@example.com', 'password': 'guanajuato2023', 'first_name': 'Instituto Tecnológico Superior de Sur de Guanajuato'},
            {'username': 'itpuebla', 'email': 'itpuebla@example.com', 'password': 'puebla2023', 'first_name': 'Instituto Tecnológico de Puebla'},
            {'username': 'ithermosillo', 'email': 'ithermosillo@example.com', 'password': 'hermosillo2023', 'first_name': 'Instituto Tecnológico de Hermosillo'},
            {'username': 'ittijuana', 'email': 'ittijuana@example.com', 'password': 'tijuana2023', 'first_name': 'Instituto Tecnológico de Tijuana'},
            {'username': 'itmochis', 'email': 'itmochis@example.com', 'password': 'mochis2023', 'first_name': 'Instituto Tecnológico de Los Mochis'},
            {'username': 'itssanluispotosi', 'email': 'itssanluispotosi@example.com', 'password': 'sanluispotosi2023', 'first_name': 'Instituto Tecnológico Superior de San Luis Potosí, Capital'},
            {'username': 'itzacatepec', 'email': 'itzacatepec@example.com', 'password': 'zacatepec2023', 'first_name': 'Instituto Tecnológico de Zacatepec'},
            {'username': 'itnogales', 'email': 'itnogales@example.com', 'password': 'nogales2023', 'first_name': 'Instituto Tecnológico de Nogales'},
            {'username': 'itlapaz', 'email': 'itlapaz@example.com', 'password': 'lapaz2023', 'first_name': 'Instituto Tecnológico de La Paz'},
            {'username': 'itmadero', 'email': 'itmadero@example.com', 'password': 'madero2023', 'first_name': 'Instituto Tecnológico de Ciudad Madero'},
            {'username': 'itdurango', 'email': 'itdurango@example.com', 'password': 'durango2023', 'first_name': 'Instituto Tecnológico de Durango'},
            {'username': 'itchihuahua', 'email': 'itchihuahua@example.com', 'password': 'chihuahua2023', 'first_name': 'Instituto Tecnológico de Chihuahua'},
            {'username': 'ittuxtla', 'email': 'ittuxtla@example.com', 'password': 'tuxtla2023', 'first_name': 'Instituto Tecnológico de Tuxtla Gutiérrez'},
            {'username': 'itlaguna', 'email': 'itlaguna@example.com', 'password': 'laguna2023', 'first_name': 'Instituto Tecnológico de La Laguna'},
            {'username': 'itlcardenas', 'email': 'itlcardenas@example.com', 'password': 'lcardenas2023', 'first_name': 'Instituto Tecnológico de Lázaro Cárdenas'},
            {'username': 'itpnegras', 'email': 'itpnegras@example.com', 'password': 'pnegras2023', 'first_name': 'Instituto Tecnológico de Piedras Negras'},
            {'username': 'itvillahermosa', 'email': 'itvillahermosa@example.com', 'password': 'villahermosa2023', 'first_name': 'Instituto Tecnológico de Villahermosa'},
            {'username': 'itcomitan', 'email': 'itcomitan@example.com', 'password': 'comitan2023', 'first_name': 'Instituto Tecnológico de Comitán'},
            {'username': 'itescarbonifera', 'email': 'itescarbonifera@example.com', 'password': 'carbonifera2023', 'first_name': 'Instituto Tecnológico de Estudios Superiores de La Región Carbonífera'},
            {'username': 'ittoluca', 'email': 'ittoluca@example.com', 'password': 'toluca2023', 'first_name': 'Instituto Tecnológico de Toluca'},
            {'username': 'itsteziutlan', 'email': 'itsteziutlan@example.com', 'password': 'teziutlan2023', 'first_name': 'Instituto Tecnológico Superior de Teziutlán'},
            {'username': 'itspuruandiro', 'email': 'itspuruandiro@example.com', 'password': 'puruandiro2023', 'first_name': 'Instituto Tecnológico Superior de Puruándiro'},
            {'username': 'tesecatepec', 'email': 'tesecatepec@example.com', 'password': 'ecatepec2023', 'first_name': 'Tecnológico de Estudios Superiores de Ecatepec'},
            {'username': 'itshuatusco', 'email': 'itshuatusco@example.com', 'password': 'huatusco2023', 'first_name': 'Instituto Tecnológico Superior de Huatusco'},
            {'username': 'ittehuacan', 'email': 'ittehuacan@example.com', 'password': 'tehuacan2023', 'first_name': 'Instituto Tecnológico de Tehuacán'},
            {'username': 'itsmonclova', 'email': 'itsmonclova@example.com', 'password': 'monclova2023', 'first_name': 'Instituto Tecnológico Superior de Monclova'},
            {'username': 'itstexmelucan', 'email': 'itstexmelucan@example.com', 'password': 'texmelucan2023', 'first_name': 'Instituto Tecnológico Superior de San Martín Texmelucan'},
            {'username': 'itistmo', 'email': 'itistmo@example.com', 'password': 'istmo2023', 'first_name': 'Instituto Tecnológico del Istmo'},
            {'username': 'ittlaxiaco', 'email': 'ittlaxiaco@example.com', 'password': 'tlaxiaco2023', 'first_name': 'Instituto Tecnológico de Tlaxiaco'},
            {'username': 'itcuauhtemoc', 'email': 'itcuauhtemoc@example.com', 'password': 'cuauhtemoc2023', 'first_name': 'Instituto Tecnológico de Ciudad Cuauhtémoc'},
            {'username': 'itguzman', 'email': 'itguzman@example.com', 'password': 'guzman2023', 'first_name': 'Instituto Tecnológico de Ciudad Guzmán'},
            {'username': 'itobregon', 'email': 'itobregon@example.com', 'password': 'obregon2023', 'first_name': 'Instituto Tecnológico de Álvaro Obregón'},
            {'username': 'itsvalladolid', 'email': 'itsvalladolid@example.com', 'password': 'valladolid2023', 'first_name': 'Instituto Tecnológico Superior de Valladolid'},
            {'username': 'itsjerez', 'email': 'itsjerez@example.com', 'password': 'jerez2023', 'first_name': 'Instituto Tecnológico Superior de Jerez'},
            {'username': 'itspapasquiaro', 'email': 'itspapasquiaro@example.com', 'password': 'papasquiaro2023', 'first_name': 'Instituto Tecnológico Superior de Santiago Papasquiaro'},
            {'username': 'itsyucatan', 'email': 'itsyucatan@example.com', 'password': 'yucatan2023', 'first_name': 'Instituto Tecnológico Superior de Sur del Estado de Yucatán'},
            {'username': 'itspedrocolonias', 'email': 'itspedrocolonias@example.com', 'password': 'pedrocolonias2023', 'first_name': 'Instituto Tecnológico Superior de San Pedro de las Colonias'},
            {'username': 'itocotlan', 'email': 'itocotlan@example.com', 'password': 'ocotlan2023', 'first_name': 'Instituto Tecnológico de Ocotlán'},
            {'username': 'itzitacuaro', 'email': 'itzitacuaro@example.com', 'password': 'zitacuaro2023', 'first_name': 'Instituto Tecnológico de Zitácuaro'},
            {'username': 'itsabasolo', 'email': 'itsabasolo@example.com', 'password': 'abasolo2023', 'first_name': 'Instituto Tecnológico Superior de Abasolo'},
        ]
        for data in users_data:
            try:
                user = User.objects.create_user(
                    username=data['username'],
                    email=data['email'],
                    password=data['password'],
                    first_name=data['first_name']
                )
                print(f'Usuario "{data["username"]}" creado exitosamente.')
            except Exception as e:
                print(f'Error al crear el usuario "{data["username"]}": {str(e)}')
        return HttpResponse('Bien')
    elif (algo == "URF"):
        users = User.objects.all()
        for user in users:
            InformacionExtraUsuario.objects.create(user=user)
            print(f'InformacionExtraUsuario creada para el usuario "{user.username}".')
        return HttpResponse('Bien')
    elif (algo == "KLN2"):
        datos = [
            {"nombre": "JORGE OMAR NAVARRETE GARCIA", "curp": "nagj020608hgtvrra7", "informacionTec": "Instituto Tecnológico de Celaya", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ROBERTO MORALES MELESIO", "curp": "momr031130hgtrlba0", "informacionTec": "Instituto Tecnológico de Celaya", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "SERGIO URBINA ARZATE", "curp": "uias030412hgtrrra6", "informacionTec": "Instituto Tecnológico de Celaya", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "SEBASTIAN AXEL HERNANDEZ RODRIGUEZ", "curp": "hers030703hgtrdba7", "informacionTec": "Instituto Tecnológico de Celaya", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "MIGUEL RAFAEL FABRICIO GUTIERREZ BLASQUEZ", "curp": "gubm030619hgttlga3", "informacionTec": "Instituto Tecnológico de Celaya", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "GABRIEL MAGANA RENDÓN", "curp": "marg020818hmngnba7", "informacionTec": "Instituto Tecnológico de Morelia", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ROBERTO CARLOS MUNOZ VILLEGAS", "curp": "muvr040420hmnxlba4", "informacionTec": "Instituto Tecnológico de Morelia", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ALDO DANIEL GUZMAN GONZALEZ", "curp": "guga040721hmnznla8", "informacionTec": "Instituto Tecnológico de Morelia", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ARTURO JIMENEZ SANTAMARIA", "curp": "jisa040802hmnmnra6", "informacionTec": "Instituto Tecnológico de Morelia", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "AXEL OROZCO PARDO", "curp": "oopa010926hmnrrxa1", "informacionTec": "Instituto Tecnológico de Morelia", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "MONICA ESTEFANIA ZAMUDIO BOLANOS", "curp": "zabm020707mmnmlna9", "informacionTec": "Instituto Tecnológico de Morelia", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "MARIA FERNANDA RODRIGUEZ MANZO", "curp": "romf020302mmndnra8", "informacionTec": "Instituto Tecnológico de Morelia", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "JULIO CESAR MARTINEZ NAVA", "curp": "manj001007hjcrvla4", "informacionTec": "Instituto Tecnológico de Morelia", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "DIEGO MURO CUEVAS", "curp": "mucd021118hntrvga6", "informacionTec": "Instituto Tecnológico de Tepic", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JADE MONSERRAT ALVARADO JIMENEZ", "curp": "aajj030813mntlmda8", "informacionTec": "Instituto Tecnológico de Tepic", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "MARCO ANTONIO VALENZUELA YERENA", "curp": "vaym020907hntlrra8", "informacionTec": "Instituto Tecnológico de Tepic", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "KEVIN ANDRES MARISCAL SERRANO", "curp": "mask050804hnerrva2", "informacionTec": "Instituto Tecnológico de Tepic", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "DEMIAN LEONARDO DE ALBERTI BRECHLIN", "curp": "aebd021209hntlrma0", "informacionTec": "Instituto Tecnológico de Tepic", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "YESSICA BEATRIZ MOO PISTE", "curp": "mopy010820mynxssa5", "informacionTec": "Instituto Tecnológico de Mérida", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ROSMAR EDUARDO ZACARIAS HERNANDEZ", "curp": "zahr010117hcscrsa0", "informacionTec": "Instituto Tecnológico de Mérida", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "OSWALDO ARTURO DURAN CASTILLO", "curp": "duco030807hynrssa0", "informacionTec": "Instituto Tecnológico de Mérida", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "LIBIA MADAI ITZÁ UITZIL", "curp": "iaul020218mynttba3", "informacionTec": "Instituto Tecnológico de Mérida", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "LEONEL ANSELMO ZUMARRAGA PECH", "curp": "zupl011020hynmcna3", "informacionTec": "Instituto Tecnológico de Mérida", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JAVIER DE JESUS HERNANDEZ TINOCO", "curp": "hetj020412htsrnva5", "informacionTec": "Instituto Tecnológico de Nuevo Laredo", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "HARRY SAMUEL LONG CISNEROS", "curp": "loch040922htsnsra6", "informacionTec": "Instituto Tecnológico de Nuevo Laredo", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ALAISA ANDRADE VALERO", "curp": "aava031016mtsnlla1", "informacionTec": "Instituto Tecnológico de Nuevo Laredo", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "SARA LIZETH SAENZ PAEZ", "curp": "saps040604mtsnzra0", "informacionTec": "Instituto Tecnológico de Nuevo Laredo", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSUE DANIEL RODRIGUEZ MUÑOZ", "curp": "romj010502htsdxsa0", "informacionTec": "Instituto Tecnológico de Nuevo Laredo", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSAFAT VAZQUEZ RODRIGUEZ", "curp": "varj020413hgtzdsa7", "informacionTec": "Instituto Tecnológico Superior de Purísima del Rincón", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ERIK NOE HERNANDEZ RAMIREZ", "curp": "here030708hgtrmra0", "informacionTec": "Instituto Tecnológico Superior de Purísima del Rincón", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JAIME DANIEL MARTINEZ NAVARRO", "curp": "manj051208hgtrvma8", "informacionTec": "Instituto Tecnológico Superior de Purísima del Rincón", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "YAEL ADAIR MONTES RODRIGUEZ", "curp": "mory030713hgtndla5", "informacionTec": "Instituto Tecnológico Superior de Purísima del Rincón", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "DIEGO ALBERTO MARTÍNEZ DE LA VEGA", "curp": "mavd021218hgtrgga5", "informacionTec": "Instituto Tecnológico Superior de Purísima del Rincón", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "YAHIR ALEXADER CALDERON CERRITOS", "curp": "cacy040608hgtlrha1", "informacionTec": "Instituto Tecnológico Superior de Sur de Guanajuato", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "OSCAR GARCIA HUERAMO", "curp": "gaho020322hgtrrsa1", "informacionTec": "Instituto Tecnológico Superior de Sur de Guanajuato", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "GERMAN JIMENEZ TORRES", "curp": "jitg010329hgtmrra1", "informacionTec": "Instituto Tecnológico Superior de Sur de Guanajuato", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ANA PATRICIA SANDOVAL NAVA", "curp": "sana040522mgtnvna5", "informacionTec": "Instituto Tecnológico Superior de Sur de Guanajuato", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "CRISTIAN CHACON VALDEZ", "curp": "cavc990730hgthlr01", "informacionTec": "Instituto Tecnológico Superior de Sur de Guanajuato", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ANGEL MIGUEL MOCTEZUMA MEDINA", "curp": "moma010102hgrcdna8", "informacionTec": "Instituto Tecnológico de Puebla", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "SARA CASTRO GONZALEZ", "curp": "cags011112mplsnra4", "informacionTec": "Instituto Tecnológico de Puebla", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ANTONIO ZAID JARAMILLO TEPAL", "curp": "jata010505hplrpna8", "informacionTec": "Instituto Tecnológico de Puebla", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "MARIO MARTIN LOPEZ RAMIREZ", "curp": "lorm030813hplpmra9", "informacionTec": "Instituto Tecnológico de Puebla", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "LUIS ANGEL HERNANDEZ HERNANDEZ", "curp": "hehl001027hmcrrsa3", "informacionTec": "Instituto Tecnológico de Puebla", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "BEATRIZ HERNANDEZ SIRIO", "curp": "hesb930113mtlrrt00", "informacionTec": "Instituto Tecnológico de Puebla", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "MAXIMILIANO CUAPA RUIZ", "curp": "curm000814hplpzxa5", "informacionTec": "Instituto Tecnológico de Puebla", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ERIC SANTIN VAZQUEZ", "curp": "save001109hplnzra5", "informacionTec": "Instituto Tecnológico de Puebla", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "JESUS ANTONIO MONTES FRANCO", "curp": "mofj040710hsrnrsa4", "informacionTec": "Instituto Tecnológico de Hermosillo", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "PABLO DE JESUS CARDOSO JIMENEZ", "curp": "cajp020702hsrrmba1", "informacionTec": "Instituto Tecnológico de Hermosillo", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "SARAH ALICIA GUTIERREZ HERNANDEZ", "curp": "guhs040820msrtrra5", "informacionTec": "Instituto Tecnológico de Hermosillo", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "MAURO ACUÑA OLIVARRIA", "curp": "auom031102hsrclra8", "informacionTec": "Instituto Tecnológico de Hermosillo", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JORGE ADRIAN TAPIA VALDEZ", "curp": "tavj011010hsrplra3", "informacionTec": "Instituto Tecnológico de Hermosillo", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "Fernando Orozco Fabre", "curp": "ooff030413hbcrbra7", "informacionTec": "Instituto Tecnológico de Tijuana", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSE MARIA MENDOZA ZAPATA", "curp": "mezm000909hbcnpra2", "informacionTec": "Instituto Tecnológico de Tijuana", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "RAUL FERREYRA GARCIA", "curp": "fegr990504hplrrl03", "informacionTec": "Instituto Tecnológico de Tijuana", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "DAMIAN ORTIZ GONZALEZ", "curp": "oigd021206hdfrnma4", "informacionTec": "Instituto Tecnológico de Tijuana", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "OCTAVIO FRIAS AVIÑA", "curp": "fiao010506hbcrvca8", "informacionTec": "Instituto Tecnológico de Tijuana", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOAQUIN ALBERTO ESPINOZA MORALES", "curp": "eimj020520hslsrqa1", "informacionTec": "Instituto Tecnológico de Los Mochis", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "MARTIN ROSARIO WONG ROMERO", "curp": "worm040801hslnmra2", "informacionTec": "Instituto Tecnológico de Los Mochis", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "LUIS ANGEL SANDOVAL CASTRO", "curp": "sacl020312hslnssa1", "informacionTec": "Instituto Tecnológico de Los Mochis", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JULIAN CEBALLOS LEYVA", "curp": "celj020130hslbyla5", "informacionTec": "Instituto Tecnológico de Los Mochis", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "LIZETH ALEJANDRA SOTO SOTO", "curp": "sosl031208mslttza6", "informacionTec": "Instituto Tecnológico de Los Mochis", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSE GERARDO COTA ALCANTAR", "curp": "coag021210hsltlra6", "informacionTec": "Instituto Tecnológico de Los Mochis", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ALEJANDRO SERNA CALVILLO", "curp": "seca020205hslrlla3", "informacionTec": "Instituto Tecnológico de Los Mochis", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ALBERTO ISAI ECHEVARRÍA CASTRO", "curp": "eeca021020hslcsla6", "informacionTec": "Instituto Tecnológico de Los Mochis", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "DANIEL ROCHA LARA", "curp": "rold011127hspcrna5", "informacionTec": "Instituto Tecnológico Superior de San Luis Potosí, Capital", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "YASMIN ALEJANDRA MARTINEZ TORRES", "curp": "maty040916msprrsa0", "informacionTec": "Instituto Tecnológico Superior de San Luis Potosí, Capital", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "YAHIR ISAI ORTA GONZALEZ", "curp": "oagy030428hsprnha6", "informacionTec": "Instituto Tecnológico Superior de San Luis Potosí, Capital", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "VICTOR DAVID MARTINEZ HERRERA", "curp": "mahv041026hsprrca1", "informacionTec": "Instituto Tecnológico Superior de San Luis Potosí, Capital", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "AZARETH GRIMALDO CARRIZALEZ", "curp": "gica040620hsprrza1", "informacionTec": "Instituto Tecnológico Superior de San Luis Potosí, Capital", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSE ALDO SALAZAR NERI", "curp": "sana030205hmslrla0", "informacionTec": "Instituto Tecnológico de Zacatepec", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "RAUL ISMAEL CASTILLO ESCUTIA", "curp": "caer040830hmsssla2", "informacionTec": "Instituto Tecnológico de Zacatepec", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSE ANGEL SANDOVAL ERAZO", "curp": "saea031111hgrnrna1", "informacionTec": "Instituto Tecnológico de Zacatepec", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "RUBEN BOTELLO LOPEZ", "curp": "bolr000617hgrtpba9", "informacionTec": "Instituto Tecnológico de Zacatepec", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "RAUL EDUARDO ESPINOZA GOMEZ", "curp": "eigr970115hmssml03", "informacionTec": "Instituto Tecnológico de Zacatepec", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "EMILIO LÓPEZ OSUNA", "curp": "looe030211hsrpsma8", "informacionTec": "Instituto Tecnológico de Nogales", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JESUS RAUL QUINTERO CASTRO", "curp": "qucj050818hsrnssa0", "informacionTec": "Instituto Tecnológico de Nogales", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "SAUL MANUEL BARAJAS MIRANDA", "curp": "bams980521hsrrrl09", "informacionTec": "Instituto Tecnológico de Nogales", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "EFRAM HERIBERTO SOBERANES CRUZ", "curp": "soce030731hsrbrfa7", "informacionTec": "Instituto Tecnológico de Nogales", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "DAVID ALEJANDRO QUIROZ CONTRERAS", "curp": "qucd030306hsrrnva9", "informacionTec": "Instituto Tecnológico de Nogales", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ALEJANDRA BARANDA ARELLANO", "curp": "baaa030309mgrrrla8", "informacionTec": "Instituto Tecnológico de Nogales", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ARLETH PAULINA CASTRO TERRAZAS", "curp": "cata030819msrsrra8", "informacionTec": "Instituto Tecnológico de Nogales", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "YUTZIL IRENE ELENES VAZQUEZ", "curp": "eevy010707msrlzta4", "informacionTec": "Instituto Tecnológico de Nogales", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ZEUS ADRIEL BOLIO COTA", "curp": "bocz030510hbsltsa2", "informacionTec": "Instituto Tecnológico de La Paz", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "FABIAN ALDAIR LOPEZ CRUZ", "curp": "locf031003hbsprba0", "informacionTec": "Instituto Tecnológico de La Paz", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSE ANTONIO AVILES SANCHEZ", "curp": "aisa020207hbsvnna1", "informacionTec": "Instituto Tecnológico de La Paz", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "LUIS HUMBERTO HUERTA VALDEZ", "curp": "huvl010922hbsrlsa2", "informacionTec": "Instituto Tecnológico de La Paz", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JORGE ANGEL MURILLO DE LA FUENTE", "curp": "mufj020505hbsrnra3", "informacionTec": "Instituto Tecnológico de La Paz", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ANGEL DANIEL CASTELLANOS CERVANTES", "curp": "cxca041007htssrna1", "informacionTec": "Instituto Tecnológico de Ciudad Madero", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "GRISSELLE MARTINEZ RENDON", "curp": "marg040930mvzrnra3", "informacionTec": "Instituto Tecnológico de Ciudad Madero", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "CRISTOPHER FLORES GONZALEZ", "curp": "fogc031026hdflnra6", "informacionTec": "Instituto Tecnológico de Ciudad Madero", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ANA JOLETTE REYES CERVANTES", "curp": "reca050406mtsyrna7", "informacionTec": "Instituto Tecnológico de Ciudad Madero", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ANGEL IMANOL INFANTE PEREZ", "curp": "iapa011204htsnrna1", "informacionTec": "Instituto Tecnológico de Ciudad Madero", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "DAVID BERUMEN CHAVEZ", "curp": "becd030925hdgrhva7", "informacionTec": "Instituto Tecnológico de Durango", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ARIANA NAJERA MARTINEZ", "curp": "nama030531mdgjrra7", "informacionTec": "Instituto Tecnológico de Durango", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSE MANUEL VAZQUEZ SALAZAR", "curp": "vasm021123hdgzlna8", "informacionTec": "Instituto Tecnológico de Durango", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "GERARDO ISRAEL GARCÍA MARTÍNEZ", "curp": "gamg040111hdgrrra9", "informacionTec": "Instituto Tecnológico de Durango", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "EDGAR AARON MONTES HERNANDEZ", "curp": "mohe040305hdgnrda8", "informacionTec": "Instituto Tecnológico de Durango", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "MAURIZIO FRANCISCO DELGADO MARTINEZ", "curp": "demm011030hchlrra8", "informacionTec": "Instituto Tecnológico de Chihuahua", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "FERNANDO PORRAS JALOMA", "curp": "pojf040326hchrlra9", "informacionTec": "Instituto Tecnológico de Chihuahua", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "VICTORIA VELÁZQUEZ GARCÍA", "curp": "vegv040607mchlrca4", "informacionTec": "Instituto Tecnológico de Chihuahua", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JESÚS ENRIQUE MENDOZA RAMÍREZ", "curp": "merj041213hchnmsa8", "informacionTec": "Instituto Tecnológico de Chihuahua", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "CÉSAR ADRIÁN PÉREZ CANO", "curp": "pecc020530hchrnsa0", "informacionTec": "Instituto Tecnológico de Chihuahua", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JUAN CARLOS ARGUELLO TORRES", "curp": "autj040520hcsrrna6", "informacionTec": "Instituto Tecnológico de Tuxtla Gutiérrez", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ALI LÓPEZ TOLEDO", "curp": "lota030222hcsplla7", "informacionTec": "Instituto Tecnológico de Tuxtla Gutiérrez", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "LEONARDO MOGUEL MORALES", "curp": "moml030404hcsgrna8", "informacionTec": "Instituto Tecnológico de Tuxtla Gutiérrez", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "IVAN CASTELLANOS SANCHEZ", "curp": "casi030304hcssnva5", "informacionTec": "Instituto Tecnológico de Tuxtla Gutiérrez", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSE ALFONSO RAMIREZ MARTINEZ", "curp": "rama011228hcsmrla6", "informacionTec": "Instituto Tecnológico de Tuxtla Gutiérrez", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "PEREZ MARQUEZ SONYA DIANET", "curp": "pems030626mclrrna1", "informacionTec": "Instituto Tecnológico de La Laguna", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ZUÑIGA PACHECO VICTOR LEONARDO", "curp": "zupv020119hclxcca1", "informacionTec": "Instituto Tecnológico de La Laguna", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "CASTRO GONZALEZ PEDRO", "curp": "cagp030727hdgsnda0", "informacionTec": "Instituto Tecnológico de La Laguna", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "MONTOYA DORADO ERNESTO GABRIEL", "curp": "mode030114hclnrra8", "informacionTec": "Instituto Tecnológico de La Laguna", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "LOZANO GONZALEZ MAX", "curp": "logm030923hclznxa6", "informacionTec": "Instituto Tecnológico de La Laguna", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JULIO SANTANA NAVARRO PICENO", "curp": "napj030410htsvclb9", "informacionTec": "Instituto Tecnológico de Lázaro Cárdenas", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ANTONIO JAVIER GONZÁLEZ LOPEZ", "curp": "gola040826hmnnpna1", "informacionTec": "Instituto Tecnológico de Lázaro Cárdenas", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "NAOMI KRYSTEL GUTIERREZ VARGAS", "curp": "guvn031229mmctrma4", "informacionTec": "Instituto Tecnológico de Lázaro Cárdenas", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "IVAN ALBERTO LARA GUTIERREZ", "curp": "lagi040317hmnrtva4", "informacionTec": "Instituto Tecnológico de Lázaro Cárdenas", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "FRANCISCO XAVIER GONZALEZ CAMACHO", "curp": "gocf010501hmnnmra8", "informacionTec": "Instituto Tecnológico de Lázaro Cárdenas", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "HÉCTOR DAVID VILLANUEVA HERNÁNDEZ", "curp": "vihh040703hcllrca6", "informacionTec": "Instituto Tecnológico de Piedras Negras", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSÉ ÁNGEL GUZMÁN HUERTA", "curp": "guha040820hclzrna6", "informacionTec": "Instituto Tecnológico de Piedras Negras", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ANA CRISTINA MENDOZA CORONADO", "curp": "meca021218mclnrna0", "informacionTec": "Instituto Tecnológico de Piedras Negras", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "VÍCTOR IVÁN GONZÁLEZ NEIRA", "curp": "gonv020905hclnrca0", "informacionTec": "Instituto Tecnológico de Piedras Negras", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "EMILIANO HERNÁNDEZ RODRÍGUEZ", "curp": "here021127hnerdma7", "informacionTec": "Instituto Tecnológico de Piedras Negras", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "URIEL PLIEGO LARA", "curp": "pilu050707htclrra1", "informacionTec": "Instituto Tecnológico de Villahermosa", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "YAMILET HERNANDEZ PEREZ", "curp": "hepy050111mtcrrma4", "informacionTec": "Instituto Tecnológico de Villahermosa", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JESUS SANTIAGO GONZALEZ MARTINEZ", "curp": "gomj031111htcnrsa7", "informacionTec": "Instituto Tecnológico de Villahermosa", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "ANDREA XIMENA FRANCO GARCIA", "curp": "faga050816mtcrrna8", "informacionTec": "Instituto Tecnológico de Villahermosa", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JOSE MANUEL LOPEZ SILVAN", "curp": "losm031101htcplna1", "informacionTec": "Instituto Tecnológico de Villahermosa", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "EMMANUEL GÓMEZ PÉREZ", "curp": "gope010731hcsmrma0", "informacionTec": "Instituto Tecnológico de Comitán", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "NEYZER JOSUÉ PÉREZ GARCÍA", "curp": "pegn050531hcsrrya3", "informacionTec": "Instituto Tecnológico de Comitán", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "CARLOS MANUEL HERNÁNDEZ HERNÁNDEZ", "curp": "hehc050816hcsrrra7", "informacionTec": "Instituto Tecnológico de Comitán", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JONATHAN EMMANUEL AGUILAR LÓPEZ", "curp": "aulj040216hcsgpna7", "informacionTec": "Instituto Tecnológico de Comitán", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "DAVID CASTILLO PÉREZ", "curp": "capd040405hcssrva5", "informacionTec": "Instituto Tecnológico de Comitán", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "URIEL ALEJADRO ROMO RODRIGUEZ", "curp": "rorp010205hclmdra7", "informacionTec": "Instituto Tecnológico de Estudios Superiores de La Región Carbonífera", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "FRANCISCO JAVIER FARIAS CAMACHO", "curp": "facf030816hclrmra4", "informacionTec": "Instituto Tecnológico de Estudios Superiores de La Región Carbonífera", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "DEBANHI ESMERALDA FERNANDEZ ALEMAN", "curp": "fead020924mclrlba3", "informacionTec": "Instituto Tecnológico de Estudios Superiores de La Región Carbonífera", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "LUIS ORLANDO DAVILA RODRIGUEZ", "curp": "darl010919hclvdsa5", "informacionTec": "Instituto Tecnológico de Estudios Superiores de La Región Carbonífera", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "MELCHOR MEDRANO BERMEA", "curp": "mebm021109hcldrla4", "informacionTec": "Instituto Tecnológico de Estudios Superiores de La Región Carbonífera", "tipoUsuario": "Participante Ciencias Básicas"},
            {"nombre": "JESUS EDUARDO CRUZ CRUZ", "curp": "cucj031208hmcrrsa4", "informacionTec": "Instituto Tecnológico de Toluca", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "EDGAR EMILIO ARZOLA AGUIRRE", "curp": "aoae020521hmcrgda0", "informacionTec": "Instituto Tecnológico de Toluca", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "FERNANDO PÉREZ GARDUÑO", "curp": "pegf021119hmcrrra5", "informacionTec": "Instituto Tecnológico de Toluca", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "MARIA JOSE MORALES DIAZ", "curp": "modj020330mplrzsa2", "informacionTec": "Instituto Tecnológico Superior de Teziutlán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "RODOLFO XOCHIATENO LUNA", "curp": "xolr030216hplcnda7", "informacionTec": "Instituto Tecnológico Superior de Teziutlán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "BRYLLYTEE DEL SOCORRO CEBALLOS NIEVES", "curp": "cenb020423mplbvra5", "informacionTec": "Instituto Tecnológico Superior de Teziutlán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "EVA XIMENA ROSAS ANDRADE", "curp": "roae011105mmnsnva9", "informacionTec": "Instituto Tecnológico Superior de Puruándiro", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ANA LAURA RODRIGUEZ HERNANDEZ", "curp": "roha971220mmndrn04", "informacionTec": "Instituto Tecnológico Superior de Puruándiro", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "JUAN FRANCISCO ZENDEJAS NAVARRO", "curp": "zenj010905hmnnvna4", "informacionTec": "Instituto Tecnológico Superior de Puruándiro", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "FERNANDA JAQUELINE RANGEL CRUZ", "curp": "racf980113mdfnrr03", "informacionTec": "Tecnológico de Estudios Superiores de Ecatepec", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "LUIS EDUARDO CARRILLO GARCIA", "curp": "cagl020927hdfrrsa9", "informacionTec": "Tecnológico de Estudios Superiores de Ecatepec", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "AXEL RICARDO CONTRERAS NIETO", "curp": "cona960409hmcntx03", "informacionTec": "Tecnológico de Estudios Superiores de Ecatepec", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "RUBEN SANCHEZ HERNANDEZ", "curp": "sahr001021hvznrba9", "informacionTec": "Instituto Tecnológico Superior de Huatusco", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "MARIA ESMERALDA MORALES RAMOS", "curp": "more021026mvzrmsa8", "informacionTec": "Instituto Tecnológico Superior de Huatusco", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ADRIANA ARENAS VELA", "curp": "aeva021227mvzrlda8", "informacionTec": "Instituto Tecnológico Superior de Huatusco", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "LUZ DEL CARMEN RUBIO DE LOS SANTOS", "curp": "rusl021013mplbnza6", "informacionTec": "Instituto Tecnológico de Tehuacán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "EIMY BELÉN LANDEROS JUÁREZ", "curp": "laje011120mplnrma5", "informacionTec": "Instituto Tecnológico de Tehuacán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "JUAN DIEGO GALICIA GUZMÁN", "curp": "gagj020907hpllzna1", "informacionTec": "Instituto Tecnológico de Tehuacán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "MONICA SARAI HERNANDEZ GARCIA", "curp": "hegm030803mclrrna9", "informacionTec": "Instituto Tecnológico Superior de Monclova", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "MIRIAM CUELLAR MENA", "curp": "cumm031015mcllnra2", "informacionTec": "Instituto Tecnológico Superior de Monclova", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "FRIDA ITZEL MUÑOZ BARRIENTOS", "curp": "mubf020524mclxrra7", "informacionTec": "Instituto Tecnológico Superior de Monclova", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ARELY SOTO SANCHEZ", "curp": "sosa020831mpltnra6", "informacionTec": "Instituto Tecnológico Superior de San Martín Texmelucan", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "LESLIE SERAFIN GALVEZ", "curp": "segl050610mplrlsa3", "informacionTec": "Instituto Tecnológico Superior de San Martín Texmelucan", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "JUAN ANTONIO RAMIREZ PACHECO", "curp": "rapj030424hplmcna5", "informacionTec": "Instituto Tecnológico Superior de San Martín Texmelucan", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "JOSE ANGEL LÓPEZ VICENTE", "curp": "lova991002hocpcn02", "informacionTec": "Instituto Tecnológico del Istmo", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "DIANA LEYDI CRUZ CABRERA", "curp": "cucd990409mocrbn06", "informacionTec": "Instituto Tecnológico del Istmo", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "MARIA FERNANDA MIGUEL RIOS", "curp": "mirf030609mocgsra6", "informacionTec": "Instituto Tecnológico del Istmo", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "DAYRA SOLEDAD ORTIZ VELASCO", "curp": "oivd030820mocrlya8", "informacionTec": "Instituto Tecnológico de Tlaxiaco", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ERIKA JAZMIN RAMOS ANTUNEZ", "curp": "raae970308mocmnr05", "informacionTec": "Instituto Tecnológico de Tlaxiaco", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "LOURDES NANCY GARCIA SILVA", "curp": "gasl910212mocrlr03", "informacionTec": "Instituto Tecnológico de Tlaxiaco", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "GLORIA MARIA QUEZADA PARRA", "curp": "qupg020306mchzrla1", "informacionTec": "Instituto Tecnológico de Ciudad Cuauhtémoc", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "JESUS COSME GRAJEDA LOYA", "curp": "galj020817hngrysa6", "informacionTec": "Instituto Tecnológico de Ciudad Cuauhtémoc", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ZURISADAI MURILLO LOPEZ", "curp": "mulz030926hchrpra9", "informacionTec": "Instituto Tecnológico de Ciudad Cuauhtémoc", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "CORINA ARIAS ORTIZ", "curp": "aioc000908mjcrrra6", "informacionTec": "Instituto Tecnológico de Ciudad Guzmán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "LUZ ESTEFANY SALAS GUTIERREZ", "curp": "sagl030206mneltza8", "informacionTec": "Instituto Tecnológico de Ciudad Guzmán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ANA MARILU AMBRIZ VERA", "curp": "aiva890228mjcmrn07", "informacionTec": "Instituto Tecnológico de Ciudad Guzmán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "XIMENA DE LA ROSA MAYA", "curp": "romx020830mdfsyma7", "informacionTec": "Instituto Tecnológico de Álvaro Obregón", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "SAMANTHA MARTINEZ ALVAREZ", "curp": "maas020129mdfrlma4", "informacionTec": "Instituto Tecnológico de Álvaro Obregón", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ANDREA MICHEL GARCIA PARDO", "curp": "gapa030617mdfrrna0", "informacionTec": "Instituto Tecnológico de Álvaro Obregón", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "DANIEL ISAI MENESES CHE", "curp": "mecd010524hynnhna4", "informacionTec": "Instituto Tecnológico Superior de Valladolid", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "LIZET GUADALUPE AY CEN", "curp": "axcl040129mynynza7", "informacionTec": "Instituto Tecnológico Superior de Valladolid", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "KEVIN AZRAIM MEDRANO PENICHE", "curp": "mepk030919hyndnva9", "informacionTec": "Instituto Tecnológico Superior de Valladolid", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "JOSE SANTOS RENE ORTIZ OLAGUE", "curp": "oios981010hzsrln02", "informacionTec": "Instituto Tecnológico Superior de Jerez", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "EVELIN NAVA ENRIQUEZ", "curp": "naee031028mzsvnva9", "informacionTec": "Instituto Tecnológico Superior de Jerez", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "MARISOL MEJIA DIOSDADO", "curp": "medm020522mzsjsra2", "informacionTec": "Instituto Tecnológico Superior de Jerez", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "PALOMA MENDOZA GAMBOA", "curp": "megp010916mdgnmla5", "informacionTec": "Instituto Tecnológico Superior de Santiago Papasquiaro", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "WENDY GÓMEZ HERNÁNDEZ", "curp": "gohw021018mdgmrna6", "informacionTec": "Instituto Tecnológico Superior de Santiago Papasquiaro", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "PAOLA MICHELL RUIZ QUIÑONES", "curp": "ruqp010920mdgzxla3", "informacionTec": "Instituto Tecnológico Superior de Santiago Papasquiaro", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ERMILA ASUNCION VILLARREAL MEJIA", "curp": "vime020816mynljra4", "informacionTec": "Instituto Tecnológico Superior de Sur del Estado de Yucatán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "MARIA YAJAIDI CAAMAL CANCHE", "curp": "cacy031109mynmnjb4", "informacionTec": "Instituto Tecnológico Superior de Sur del Estado de Yucatán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "GISSEL NATALY TUN AVILA", "curp": "tuag001027mynnvsa9", "informacionTec": "Instituto Tecnológico Superior de Sur del Estado de Yucatán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ESTRADA CISNEROS ILSE LIZAYTH", "curp": "eaci021213mclssla9", "informacionTec": "Instituto Tecnológico Superior de San Pedro de las Colonias", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "CHAVARRIA ALVARADO LUIS MANUEL", "curp": "caal030516hclhlsa9", "informacionTec": "Instituto Tecnológico Superior de San Pedro de las Colonias", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ESQUIVEL MONSIVAIS JOSE FRANCISCO", "curp": "eumf021118hclsnra6", "informacionTec": "Instituto Tecnológico Superior de San Pedro de las Colonias", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "NOÉ BUSTOS SAAVEDRA", "curp": "busn011024hjcsvxa9", "informacionTec": "Instituto Tecnológico de Ocotlán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "HANNIA MAGDALENA FLORES CARRILLO", "curp": "foch021220mjclrna1", "informacionTec": "Instituto Tecnológico de Ocotlán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "PEDRO ISRAEL SANCHEZ PEREZ", "curp": "sapp011128hjcnrda7", "informacionTec": "Instituto Tecnológico de Ocotlán", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "SEBASTIAN ITZAMNA MEDINA CONTRERAS", "curp": "mecs000707hmndnba1", "informacionTec": "Instituto Tecnológico de Zitácuaro", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "BRENDA ESQUIVEL GARCIA", "curp": "eugb030622mmnsrra8", "informacionTec": "Instituto Tecnológico de Zitácuaro", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "YAHIR AVILES JAIMEZ", "curp": "aijy030426hmnvmha1", "informacionTec": "Instituto Tecnológico de Zitácuaro", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "ANA DANIELA ZARATE CRISANTO", "curp": "zaca011211mgtrrna5", "informacionTec": "Instituto Tecnológico Superior de Abasolo", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "JAZMIN ETHELVINA SAAVEDRA MARTINEZ", "curp": "samj020310mgtvrza4", "informacionTec": "Instituto Tecnológico Superior de Abasolo", "tipoUsuario": "Participante Económico Administrativo"},
            {"nombre": "PAOLA MARTINEZ GARCIA", "curp": "magp030521mgtrrla2", "informacionTec": "Instituto Tecnológico Superior de Abasolo", "tipoUsuario": "Participante Económico Administrativo"}
        ]


        # Itera sobre los datos y crea instancias de Usuarios
        for dato in datos:
            try:
                infoTec = InformacionExtraUsuario.objects.get(user__first_name=dato["informacionTec"])
                hotelq = Hotel.objects.get(nombreHotel = "Best Western PLUS Gran Hotel Morelia")
                # Realiza las operaciones necesarias con infoTec
                usuario = Usuarios.objects.create(
                    nombre=dato["nombre"],
                    curp=dato["curp"].upper(),
                    informacionTec=infoTec,
                    tipoUsuario=dato["tipoUsuario"],
                    hotel= hotelq
                )
                print(f'Usuario creado para el usuario "{usuario.nombre}".')
            except ObjectDoesNotExist as i:
                # Manejar la excepción cuando el objeto no existe
                print("El objeto InformacionExtraUsuario no existe para el nombre proporcionado." + dato["informacionTec"])
                print(i)
            except Exception as e:
                # Manejar otras excepciones que puedan ocurrir durante la consulta
                print(f"Error: {str(e)}")
        return HttpResponse('Bien')

    return HttpResponse('Mal')