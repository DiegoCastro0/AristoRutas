from django.db import models
from Usuarios.models import Usuario  

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
