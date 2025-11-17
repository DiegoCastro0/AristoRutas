"""
URL configuration for Aristoruta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from MenuP import views as menu_views
from Rutas import views as rutas_views
from Login import views as login_views
from Iniciar import views as iniciar_views
from QuienesSomos import views as quienes_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_views.Menu, name='home'),
    path('Rutas/', rutas_views.Rutas, name='rutas'),
    path('login/', login_views.login_view, name="login"),
    path('iniciar/', iniciar_views.iniciar_sesion_view, name='iniciar_sesion'),
    path('quienes_somos/', quienes_views.Quienes, name='quienes'),
    path('urbanas/', rutas_views.urbanas, name='urbanas'),
    path('interurbanas/', rutas_views.interurbanas, name='interurbanas'),
    path('interdepartamentales/', rutas_views.interdepartamentales, name='interdepartamentales'),
   
]
