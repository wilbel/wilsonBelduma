"""beldumaWilson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path , include
from . import views
from  personas.views import FormularioPersonaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('personas/', include('personas.urls')),
    path('paises/', FormularioPersonaView.get_pais),
    path('nacionalidad/<int:idpais>', FormularioPersonaView.get_nacionalidad),
    path('registrarPersona/',FormularioPersonaView.index, name="registrarPersona"),
    path('savePersona/',FormularioPersonaView.procesar_formulario, name="savePersona"),
    path('form_actualizar/<int:id>',FormularioPersonaView.showformActualizar),
    path('actualizar/<int:id>', FormularioPersonaView.actualizarPersona),
]
