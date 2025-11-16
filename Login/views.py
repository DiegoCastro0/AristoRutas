from django.shortcuts import render, redirect
from Usuarios.models import Usuario
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')

        if Usuario.objects.filter(usuario=usuario).exists():
            return render(request, 'login.html', {'error': 'El usuario ya existe'})

        Usuario.objects.create(usuario=usuario, contraseña=clave)
        return redirect('iniciar_sesion')

    return render(request, 'login.html')


