from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages

Usuario = get_user_model()

# --- LOGIN ---
def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')

        user = authenticate(request, usuario=usuario, password=clave)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, 'login.html', {'modo': 'login'})

# --- REGISTRO ---
def registro_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        clave = request.POST.get('clave')

        if Usuario.objects.filter(usuario=usuario).exists():
            return render(request, 'login.html', {'error': 'El usuario ya existe', 'modo': 'registro'})

        Usuario.objects.create_user(usuario=usuario, email=email, password=clave)
        return redirect('iniciar_sesion')

    return render(request, 'login.html', {'modo': 'registro'})

# --- LOGOUT MANUAL (El que arregla el error 405) ---
def logout_view(request):
    logout(request)
    return redirect('iniciar_sesion')