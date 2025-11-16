from django.shortcuts import render, redirect
from Usuarios.models import Usuario

def iniciar_sesion_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')

        try:
            user = Usuario.objects.get(usuario=usuario)
            if user.contraseña == clave:
                # Aquí puedes agregar lógica extra si lo deseas
                return redirect('home')  # Redirige al panel principal
            else:
                return render(request, 'iniciar.html', {'error': 'Contraseña incorrecta'})
        except Usuario.DoesNotExist:
            return render(request, 'iniciar.html', {'error': 'Usuario no encontrado'})

    return render(request, 'iniciar.html')