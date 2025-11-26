def user_plan(request):
    """Context processor que añade la variable `plan` a todas las plantillas.

    Si el usuario no está autenticado devuelve 'Gratuito'. Si hay problemas
    con la base de datos, devuelve 'Gratuito' para evitar romper la plantilla.
    """
    try:
        if not request.user.is_authenticated:
            return {'plan': 'Gratuito'}
        # Importar aquí para evitar errores durante la carga de settings/apps
        from Servicios.models import Pago
        ultimo = Pago.objects.filter(usuario=request.user).order_by('-fecha_pago').first()
        return {'plan': (ultimo.plan if ultimo else 'Gratuito')}
    except Exception as e:
        # En desarrollo conviene ver el error en consola/logs; devolvemos 'Gratuito' para no romper las plantillas
        print('user_plan context processor error:', e)
        return {'plan': 'Gratuito'}
