import os
from pathlib import Path

# BASE_DIR = racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Sécurité
SECRET_KEY = 'django-insecure-<remplace_par_ta_cle_secrete>'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',  # ton app personnalisée
]

# Middlewares (ordre important)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL de l'application
ROOT_URLCONF = 'config.urls'

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # dossier global pour les templates
        'APP_DIRS': True,  # pour que Django cherche aussi dans chaque app, dans un dossier 'templates'
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # ajouter ici d’autres context processors si besoin
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# Base de données (SQLite par défaut)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Langue et fuseau horaire
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Fichiers statiques
STATIC_URL = '/static/'

# Dossier de stockage (si besoin)
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'liste_maisons'
LOGOUT_REDIRECT_URL = 'connexion'
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
