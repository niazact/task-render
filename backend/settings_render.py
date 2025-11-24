import os 
import dj_database_url
from .settings import *
from .settings import BASE_DIR
ALLOWED_HOSTS =[os.environ.get['RENDER_EXTERNAL_HOSTNAME'], 'localhost', ]
CSRF_TRUSTED_ORIGINS=['https://' + os.environ.get['RENDER_EXTERNAL_HOSTNAME']] 
DEBUG =False
SECRET_KEY = os.environ.get['SECRET_KEY']  

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #This is used to serve static files in production.
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ALLOWED_ORIGINS = [
#      "https://tasklist.mizantechs.com" ,#This is the host domain for the react app (PRODUCTION)
   
# ]



STORAGES ={
    "default": {
        'BACKEND': "django.core.files.storage.FileSystemStorage",   
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    
}

DATABASES = {

    'default': dj_database_url.config(
        default = os.environ.get['DATABASE_URL'],
        conn_max_age=600,
    )
}



