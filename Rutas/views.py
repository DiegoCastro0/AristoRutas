from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Sugerencia
from .models import RutaBus

def Rutas(request):
    return render(request, 'rutas.html')

def urbanas(request):
    rutas = RutaBus.objects.filter(tipo='Urbana', estado='Activa')
    return render(request, 'urbanas.html', {'rutas': rutas})

def interurbanas(request):
    rutas = RutaBus.objects.filter(tipo='Interurbana', estado='Activa')
    # Renderiza la plantilla con la lista de rutas (la plantilla actual se llama 'Interurbanas.html')
    return render(request, 'Interurbanas.html', {'rutas': rutas})

def interdepartamentales(request):
    rutas = RutaBus.objects.filter(tipo='Interdepartamental', estado='Activa')
    return render(request, 'interdepartamentales.html', {'rutas': rutas})

@login_required
def sugerencias(request):
    if request.method == 'POST':
        usuario = request.user  # instancia de tu modelo Usuario
        comentario = request.POST.get('sugerencia')  

        if not comentario:
            messages.error(request, "El comentario no puede estar vacío.")
            return render(request, 'sugerencias.html', {'sugerencias': Sugerencia.objects.filter(usuario=usuario)})

        # Crear la sugerencia
        Sugerencia.objects.create(
            usuario=usuario,
            nombre_usuario=usuario.usuario,
            comentario=comentario
        )

        messages.success(request, "Sugerencia enviada correctamente.")
        return redirect('sugerencias')  # redirige para evitar duplicados si refresca
    
    # Mostrar sugerencias del usuario
    usuario = request.user
    sugerencias_usuario = Sugerencia.objects.filter(usuario=usuario).order_by('-fecha_creacion')
    return render(request, 'sugerencias.html', {'sugerencias': sugerencias_usuario})

