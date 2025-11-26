from django.contrib import admin
from django.urls import path, include

from MenuP import views as menu_views
from Rutas import views as rutas_views
from Login import views as login_views 
from QuienesSomos import views as quienes_views
from Servicios import views as Servicios_views
from Rutas import views as Rutas_views
from Rutas import views as Reportes_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_views.Menu, name='home'),
    path('Rutas/', rutas_views.Rutas, name='rutas'),

    # Login y registro
    path('login/', login_views.login_view, name='iniciar_sesion'),
    path('registro/', login_views.registro_view, name='registro'),
    
    # USAMOS TU FUNCIÓN MANUAL (Esto arregla el error Method Not Allowed)
    path('logout/', login_views.logout_view, name='salir'),

    # Esto habilita SOLO el cambio de contraseña
    path('accounts/', include('django.contrib.auth.urls')),

    # Otras vistas
    path('quienes_somos/', quienes_views.Quienes, name='quienes'),
    path('Rutas/urbanas/', rutas_views.urbanas, name='urbanas'),
    path('Rutas/interurbanas/', rutas_views.interurbanas, name='interurbanas'),
    path('Rutas/interdepartamentales/', rutas_views.interdepartamentales, name='interdepartamentales'),
    path('Rutas/sugerencias/', rutas_views.sugerencias, name='sugerencias'),
    path('Servicios/', Servicios_views.upgrade_plan, name='upgrade_plan'),
    path('Rutas/donde-voy/', Rutas_views.donde_voy, name='donde_voy'),
    path('Rutas/reportes', Reportes_views.reportes, name='reportes'),
]