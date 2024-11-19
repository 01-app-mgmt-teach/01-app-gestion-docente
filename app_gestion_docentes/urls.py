"""
URL configuration for app_gestion_docentes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from autenticacion.views import inicio_sesion, crear_cuenta, cerrar_sesion
from autenticacion.views import *
from pagina_principal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagina_principal.urls')),
    # path('autenticacion/', include('autenticacion.urls'), name='autenticacion'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('crear_cuenta/', crear_cuenta, name='crear_cuenta'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('perfil/', perfil_usuario_actual, name='perfil_usuario_actual'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
]
