from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML,CSS
import weasyprint
from enecb import settings
import os

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def credencial(request):
    if request.method == "POST":
        template = get_template("credenciales/credencialesFront.html")
        context = {"name":"CredencialFrente"}
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
    else:
        return render(request, 'credenciales/mostrarCredenciales.html')

