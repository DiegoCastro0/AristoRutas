from django.db import models
from Usuarios.models import Usuario
from decimal import Decimal

class Pago(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="pagos"
    )
    plan = models.CharField(max_length=50)  # Nombre del plan elegido
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    metodo = models.CharField(
        max_length=50,
        choices=[('Tarjeta', 'Tarjeta')],  # Solo tarjeta
        default='Tarjeta'
    )
    referencia = models.CharField(max_length=100, unique=True)  # Número de transacción o comprobante
    fecha_pago = models.DateTimeField(auto_now_add=True)  # Se guarda automáticamente al crear el registro
    verificado = models.BooleanField(default=False)  # Estado de validación del pago

    class Meta:
        db_table = "servicios_pago"   # nombre explícito de la tabla

    def __str__(self):
        return f"Pago {self.referencia} - Usuario {self.usuario.id} - {self.monto}"
