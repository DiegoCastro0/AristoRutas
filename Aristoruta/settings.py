"""
Django settings for Aristoruta project.
"""

from pathlib import Path
import os
import dj_database_url

# Rutas base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.getenv("SECRET_KEY", "insecure-key")
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "aristorutas-production.up.railway.app",  # dominio Railway
    "localhost",
    "127.0.0.1"
]

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # tus aplicaciones
    'MenuP',
    'Rutas',
    'Usuarios',
    'Login',
    'QuienesSomos',
    'Servicios',
]

# Modelo de usuario personalizado
AUTH_USER_MODEL = 'Usuarios.Usuario'

# Configuración de login/logout
LOGIN_URL = 'iniciar_sesion'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # sirve archivos estáticos en producción
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de URLs y templates
ROOT_URLCONF = 'Aristoruta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Usuarios.context_processors.user_plan',
            ],
        },
    },
]

WSGI_APPLICATION = 'Aristoruta.wsgi.application'


# Base de datos (Railway inyecta DATABASE_URL automáticamente)
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL")
    )
}



# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = []

# Internacionalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/El_Salvador'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]   # carpeta local de estáticos
STATIC_ROOT = BASE_DIR / "staticfiles"     # carpeta que Whitenoise sirve en Railway

# Optimización de archivos estáticos
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Primary key por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
