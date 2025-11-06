from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mascotas, name='lista_mascotas'),
    path('registrar/', views.registrar_mascota, name='registrar_mascota'),
]
