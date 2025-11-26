from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import hashlib

from Servicios.models import Pago

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


@login_required
def perfil_view(request):
    user = request.user

    # Último pago (si existe) para determinar el plan activo
    ultimo_pago = Pago.objects.filter(usuario=user).order_by('-fecha_pago').first()
    plan_actual = ultimo_pago.plan if ultimo_pago else 'Gratuito'
    pagos_count = Pago.objects.filter(usuario=user).count()
    ultimo_pago_fecha = ultimo_pago.fecha_pago if ultimo_pago else None

    # Gravatar por email (fallback a identicon)
    email = (user.email or '').strip().lower().encode('utf-8')
    email_hash = hashlib.md5(email).hexdigest() if email else ''
    avatar_url = f"https://www.gravatar.com/avatar/{email_hash}?s=200&d=identicon"

    context = {
        'user_obj': user,
        'plan_actual': plan_actual,
        'pagos_count': pagos_count,
        'ultimo_pago_fecha': ultimo_pago_fecha,
        'avatar_url': avatar_url,
    }
    return render(request, 'perfil.html', context)