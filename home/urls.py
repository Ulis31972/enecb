from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import viewsKLN

urlpatterns = [
    path('', views.indexFormal, name="indexFormal"),
    # path('index', views.index, name="index"),
    path('credencial/<int:id>', views.credencial, name="credencial"),
    path('login/', views.loginView, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/asistencia/<int:id>', views.registroAsistencia, name="registroAsistencia"),
    path('registro/lista/<str:msg>', views.registroLista, name="registroLista"),
    path('registro/lista/actualizar/<int:id>', views.registroListaActualizar, name="registroListaActualizar"),
    path('registro/lista/crear/usuario', views.registroListaCrear, name="registroListaCrear"),
    path('horario', views.horario, name="horario"),
    path('perfil', views.perfil, name="perfil"),
    path('perfil/itinerario', views.addItinerario, name="addItinerario"),
    # path('registro', views.registro, name="registro"),
    path('scripts/<str:algo>', viewsKLN.kln, name='scripts'),
    path('lista/usuarios/', views.listaUsuariosTecnologicos, name='listaUsuariosTecnologicos'),
    path('lista/usuarios/<int:id>/', views.actualizarUsuario, name='actualizarUsuario'),
    path('descarga/pdf/<int:id>/', views.credencialPDF, name='credencialPDF'),
    path('descarga/all/<int:rango>', views.credencialall, name='credencialall')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
