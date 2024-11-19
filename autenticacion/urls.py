from django.urls import path
from .views import *

urlpatterns = [
    # path('', autenticacion, name='autenticacion'),
    # path('', autenticacion, name='autenticacion'),
    # path('crear_cuenta/<str:tipo_usuario>/', crear_cuenta, name='crear_cuenta'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('crear_cuenta/', crear_cuenta, name='crear_cuenta'),
    # path('crear_cuenta_alumno/', crear_cuenta_alumno, name='crear_cuenta_alumno'),
    # path('crear_cuenta_docente/', crear_cuenta_docente, name='crear_cuenta_docente'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('perfil/', perfil_usuario_actual, name='perfil_usuario_actual'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
]
