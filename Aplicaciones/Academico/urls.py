#Archivo para gestionar las rutas de Academico

from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cerrarSesion/', views.cerrarSesion, name="cerrarSesion"),
    path('register/', views.register, name="register"),
    path('eliminarCurso/<codigo>', views.eliminarCurso)

]
