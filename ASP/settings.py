"""
Django settings for ASP project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from getenv import env
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRETKEY", '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", True)
TEMPLATE_DEBUG = DEBUG

ADMINS = (('Arlefreak','arlefreak@gmail.com'),)
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'asp.herokuapp.com',
    'a-sp.mx',
    'www.a-sp.mx',
    'smtp.gmail.com',
    'aspsite.s3.amazonaws.com']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'solo',
    'ckeditor',
    'imagekit',
    'collectfast',
    'embed_video',
    'portfolio',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'portfolio.context_processors.menu',
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'ASP.urls'

WSGI_APPLICATION = 'ASP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ASPDB',
            'USER': 'arlefreak',
            'PASSWORD': env("DBPASSWD"),
            'HOST': 'localhost',
            'PORT': '',
            }
        }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-Mx'
ugettext = lambda s: s

LANGUAGES = (
    ('es-Mx', ugettext('Spanish')),
    ('en', ugettext('English')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID',False)
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY',False)
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME',False)
AWS_STORAGE_BUCKET_NAME='aspsite'
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
COLLECTFAST_ENABLED = True
CKEDITOR_UPLOAD_PATH = STATIC_URL + 'uploads/'
IMAGEKIT_DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

#Email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'arlefreak@gmail.com'
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', False)
EMAIL_PORT = 587
