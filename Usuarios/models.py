from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, email, password=None, **extra_fields):
        if not usuario:
            raise ValueError("El usuario debe tener un nombre de usuario")
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        email = self.normalize_email(email)
        user = self.model(usuario=usuario, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(usuario, email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    usuario = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.usuario
