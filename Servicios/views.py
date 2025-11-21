from django.shortcuts import render, redirect
from .models import Pago
from decimal import Decimal
import uuid

def upgrade_plan(request):
    if request.method == "POST":
        plan = request.POST.get("plan")
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        tarjeta = request.POST.get("tarjeta")
        vencimiento = request.POST.get("vencimiento")
        cvv = request.POST.get("cvv")

        # Generar referencia única
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

        # 🔎 Simulación de verificación bancaria
        # Regla simple: si la tarjeta empieza con "4111" y el CVV es "123", se aprueba
        if tarjeta.startswith("4111") and cvv == "123":
            verificado = True
        else:
            verificado = False

        # Crear registro en la BD con estado de verificación
        Pago.objects.create(
            usuario=request.user,   # requiere que el usuario esté autenticado
            plan=plan,
            monto=monto,
            metodo="Tarjeta",
            referencia=referencia,
            verificado=verificado
        )

        # Redirigir a la misma página o a una de confirmación
        return redirect("upgrade_plan")

    # Si es GET, solo renderiza la plantilla
    return render(request, "upgrade_plan.html")
