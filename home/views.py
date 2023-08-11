from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def credencial(request):
    return render(request, 'credenciales/credencialesFront.html')

