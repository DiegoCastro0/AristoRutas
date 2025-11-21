from django.db import models
from Usuarios.models import Usuario
from decimal import Decimal

class Sugerencia(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="sugerencias"
    )

    nombre_usuario = models.CharField(max_length=150)  


    comentario = models.TextField()                   
    
    fecha_creacion = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"UsuarioID: {self.usuario.id} | Nombre: {self.nombre_usuario} | Fecha: {self.fecha_creacion} | Comentario: {self.comentario[:30]}"

class RutaBus(models.Model):
    """
    Modelo que representa una ruta de bus en la base de datos.

    Atributos:
        nombre_ruta (CharField): Nombre identificador de la ruta.
        origen (CharField): Punto de partida de la ruta.
        destino (CharField): Punto de llegada de la ruta.
        paradas (JSONField): Lista de paradas intermedias en formato JSON.
        link (URLField): Enlace externo asociado a la ruta (ej. mapa).
        imagen (CharField): Ruta o nombre del archivo de imagen representativa.
        estado (CharField): Estado de la ruta, puede ser 'Activa' o 'Inactiva'.
        tipo (CharField): Clasificación de la ruta: 'Urbana', 'Interurbana' o 'Interdepartamental'.
        ultima_actualizacion (DateTimeField): Fecha y hora de la última modificación.
    """

    nombre_ruta = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    paradas = models.JSONField()
    link = models.URLField(max_length=255)
    imagen = models.CharField(max_length=255)
    estado = models.CharField(
        max_length=20,
    choices=[('Activa', 'Activa'), ('Inactiva', 'Inactiva')],
        default='Activa'
    )
    tipo = models.CharField(
        max_length=30,
        choices=[
            ('Urbana', 'Urbana'),
            ('Interurbana', 'Interurbana'),
            ('Interdepartamental', 'Interdepartamental'),
        ],
        default='Urbana'
    )
    tarifa = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('0.00'))
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Configuración del modelo:
            db_table: Nombre explícito de la tabla en PostgreSQL.
            managed: Indica que Django gestiona la creación y migraciones.
        """
        db_table = "rutas_buses"
        managed = True

    def __str__(self):
        """Representación legible del objeto en el admin y shell."""
        return f"{self.nombre_ruta} ({self.tipo})"