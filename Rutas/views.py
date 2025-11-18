from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def Rutas(request):
    return render(request, 'rutas.html')

def urbanas(request):
    return render(request, 'urbanas.html')

def interurbanas(request):
    return render(request, 'interurbanas.html')

def interdepartamentales(request):
    return render(request, 'interdepartamentales.html')


def sugerencias(request):
    """Renderiza la página de sugerencias.

    Solo permite el acceso si la petición proviene de la sección Rutas (comprobando el HTTP_REFERER).
    Si no, redirige a la página de rutas.
    """
    referer = request.META.get('HTTP_REFERER', '')
    # Permitir si el referer contiene la ruta de Rutas (esto no es 100% seguro, pero cumple la necesidad solicitada)
    if '/Rutas' in referer or referer.endswith('/Rutas') or referer.endswith('/Rutas/'):
        return render(request, 'sugerencias.html')
    # Si no viene desde Rutas, redirigir a la lista de rutas
    return redirect('rutas')