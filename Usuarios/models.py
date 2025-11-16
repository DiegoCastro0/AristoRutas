from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=150, unique=True)
    contraseña = models.CharField(max_length=150)

    def __str__(self):
        return self.usuario

    class Meta:
        app_label = 'Usuarios'
