from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Sugerencia, RutaBus
from Servicios.models import Pago
from django.core.paginator import Paginator
from Rutas.models import RutaBus

def obtener_plan_activo(usuario):
    if not getattr(usuario, "is_authenticated", False):
        return "Gratuito"
    pago = Pago.objects.filter(usuario=usuario, verificado=True).order_by('-fecha_pago').first()
    return pago.plan if pago else "Gratuito"

def Rutas(request):
    return render(request, 'rutas.html')


def urbanas(request):
    rutas_list = RutaBus.objects.filter(tipo='Urbana', estado='Activa').order_by('id')
    paginator = Paginator(rutas_list, 4)
    rutas = paginator.get_page(request.GET.get('page'))

    plan = obtener_plan_activo(request.user)
    return render(request, 'urbanas.html', {'rutas': rutas, 'plan': plan})

def interurbanas(request):
    rutas_list = RutaBus.objects.filter(tipo='Interurbana', estado='Activa').order_by('id')
    paginator = Paginator(rutas_list, 4)
    rutas = paginator.get_page(request.GET.get('page'))

    plan = obtener_plan_activo(request.user)
    return render(request, 'interurbanas.html', {'rutas': rutas, 'plan': plan})

def interdepartamentales(request):
    rutas_list = RutaBus.objects.filter(tipo='Interdepartamental', estado='Activa').order_by('id')
    paginator = Paginator(rutas_list, 4)
    rutas = paginator.get_page(request.GET.get('page'))

    plan = obtener_plan_activo(request.user)
    return render(request, 'interdepartamentales.html', {'rutas': rutas, 'plan': plan})

@login_required
def reportes(request):
    plan = obtener_plan_activo(request.user)

    if plan not in ["Premium Avanzado", "Premium Institucional"]:
        messages.error(request, "Tu plan no permite acceder al apartado de reportes.")
        return redirect("rutas")  # redirige a rutas si no tiene acceso

    # Aquí puedes preparar la información de reportes
    data = {
        "total_rutas": 50,  # ejemplo
        "rutas_activas": 40,
        "rutas_inactivas": 10,
    }

    return render(request, "reportes.html", {"plan": plan, "data": data})


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
