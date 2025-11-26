from django.shortcuts import render
from django.contrib import messages
from .models import Pago
from decimal import Decimal
import uuid

def upgrade_plan(request):
    if request.method == "POST":
        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            # Mensaje remarcado en el modal
            messages.error(request, "⚠️ Debes iniciar sesión para acceder a servicios.")
            return render(request, "upgrade_plan.html")

        plan = request.POST.get("plan")
        tarjeta = request.POST.get("tarjeta")
        vencimiento = request.POST.get("vencimiento")
        cvv = request.POST.get("cvv")

        referencia = str(uuid.uuid4())

        # Asignar monto según plan
        if plan == "Premium Básico":
            monto = Decimal("4.99")
        elif plan == "Premium Avanzado":
            monto = Decimal("9.99")
        elif plan == "Premium Institucional":
            monto = Decimal("29.99")
        else:
            monto = Decimal("0.00")

        # Simulación de verificación bancaria
        verificado = tarjeta.startswith("4111") and cvv == "123"

        # Crear registro en la BD
        Pago.objects.create(
            usuario=request.user,
            plan=plan,
            monto=monto,
            metodo="Tarjeta",
            referencia=referencia,
            verificado=verificado
        )

        messages.success(request, "✅ Tu pago ha sido registrado.")
        return render(request, "upgrade_plan.html")

    return render(request, "upgrade_plan.html")
