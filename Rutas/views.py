from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Sugerencia

def Rutas(request):
    return render(request, 'rutas.html')

def urbanas(request):
    return render(request, 'urbanas.html')

def interurbanas(request):
    return render(request, 'interurbanas.html')

def interdepartamentales(request):
    return render(request, 'interdepartamentales.html')

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