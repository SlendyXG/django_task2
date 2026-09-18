import os

from environs import Env

env = Env()
env.read_env()

DB_HOST = env.str('DB_HOST')
DB_PORT = env.str('DB_PORT')
DB_PASSWORD = env.str('DB_PASSWORD')
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': DB_PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

DEBUG = DEBUG

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'