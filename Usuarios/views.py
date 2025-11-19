from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Opcional: campos extra
    # ejemplo: display_name = models.CharField(max_length=150, blank=True)
    pass