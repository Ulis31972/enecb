from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.indexFormal, name="indexFormal"),
    path('index', views.index, name="index"),
    path('credencial', views.credencial, name="credencial"),
    path('login/', views.loginView, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/asistencia/<int:id>', views.registroAsistencia, name="registroAsistencia"),
    path('horario', views.horario, name="horario"),
    path('perfil', views.perfil, name="perfil"),
    # path('registro', views.registro, name="registro"),
    path('scripts/<str:algo>', views.kln, name='scripts')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
