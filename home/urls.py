from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('credencial', views.credencial, name="credencial"),
    path('login/', views.loginView, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]