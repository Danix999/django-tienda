from pathlib import Path

# --- RUTAS BASE ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SEGURIDAD (para desarrollo) ---
SECRET_KEY = "dev-secret-key-cambia-esto-en-produccion"
DEBUG = True
ALLOWED_HOSTS: list[str] = []

# --- APLICACIONES ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # App del proyecto
    "tienda",
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --- URLS RAÍZ ---
ROOT_URLCONF = "core.urls"

# --- TEMPLATES ---
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Si en el futuro quieres una carpeta global /templates, añádela aquí:
        "DIRS": [],  # [BASE_DIR / "templates"]
        "APP_DIRS": True,  # busca en app/templates
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# --- WSGI ---
WSGI_APPLICATION = "core.wsgi.application"

# --- BASE DE DATOS (SQLite para desarrollo) ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- VALIDADORES DE PASSWORD (puedes desactivar en dev si molesta) ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- IDIOMA Y ZONA HORARIA ---
LANGUAGE_CODE = "es"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

# --- ARCHIVOS ESTÁTICOS ---
STATIC_URL = "static/"
# Con APP_DIRS=True, Django ya encuentra tienda/static/
# Si luego creas /static global en la raíz, descomenta:
# STATICFILES_DIRS = [BASE_DIR / "static"]

# --- CONFIG EXTRA ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
