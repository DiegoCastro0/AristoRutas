from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Sugerencia, RutaBus


def Rutas(request):
    return render(request, 'rutas.html')


def urbanas(request):
    rutas = RutaBus.objects.filter(tipo='Urbana', estado='Activa')
    return render(request, 'urbanas.html', {'rutas': rutas})


def interurbanas(request):
    rutas = RutaBus.objects.filter(tipo='Interurbana', estado='Activa')
    return render(request, 'Interurbanas.html', {'rutas': rutas})


def interdepartamentales(request):

    rutas_list = RutaBus.objects.filter(tipo='Interdepartamental', estado='Activa').order_by('id')
    paginator = Paginator(rutas_list, 4)

    page_number = request.GET.get('page')


    rutas = paginator.get_page(page_number)


    return render(request, 'interdepartamentales.html', {'rutas': rutas})


@login_required
def sugerencias(request):
    usuario = request.user

    if request.method == 'POST':
        comentario = request.POST.get('sugerencia')

        if not comentario:
            messages.error(request, "El comentario no puede estar vacío.")
        else:
            Sugerencia.objects.create(
                usuario=usuario,
                nombre_usuario=usuario.usuario,
                comentario=comentario
            )
            messages.success(request, "Sugerencia enviada correctamente.")
            return redirect('sugerencias')

    sugerencias_usuario = Sugerencia.objects.filter(
        usuario=usuario
    ).order_by('-fecha_creacion')

    return render(request, 'sugerencias.html', {'sugerencias': sugerencias_usuario})


def donde_voy(request):
    rutas_sugeridas = RutaBus.objects.none()

    modo = request.GET.get('modo', 'manual')
    origen = request.GET.get('origen', '').strip()
    destino = request.GET.get('destino', '').strip()
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    if request.GET:
        qs = RutaBus.objects.filter(estado='Activa')

        if origen:
            qs = qs.filter(
                Q(origen__icontains=origen) |
                Q(paradas__icontains=origen)
            )

        if destino:
            qs = qs.filter(
                Q(destino__icontains=destino) |
                Q(paradas__icontains=destino)
            )

        if modo == 'gps' and lat and lon:
            # lógica futura con coordenadas 
            pass

        rutas_sugeridas = qs.distinct()

    context = {
        'rutas_sugeridas': rutas_sugeridas,
        'modo': modo,
        'origen': origen,
        'destino': destino,
        'lat': lat,
        'lon': lon,
    }
    return render(request, 'donde_voy.html', context)
