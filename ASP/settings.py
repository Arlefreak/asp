"""
Django settings for ASP project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x3*80$lqv0pxe&m8ccge-sv+-j7_%-t_x+d@f(a+!@43e8_*3l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)
DEBUG = False
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
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dkg3a5kp14qh0',                      # Or path to database file if using sqlite3.
        'USER': 'nrtyeidjtprifm',
        'PASSWORD': 'ppxS0dRM24fc8oa7KyEk5TBDfE',
        'HOST': 'ec2-54-225-168-181.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',

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

if DEBUG:
    COLLECTFAST_ENABLED = False
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'
    CKEDITOR_UPLOAD_PATH = STATIC_URL + 'uploads/'
else:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID',False)
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY',False)
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME',False)
    AWS_STORAGE_BUCKET_NAME = 'aspsite'
    AWS_QUERYSTRING_AUTH = False
    AWS_PRELOAD_METADATA = True
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
    COLLECTFAST_ENABLED = True
    CKEDITOR_UPLOAD_PATH = STATIC_URL + 'uploads/'

#Email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'arlefreak@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', False)
EMAIL_PORT = 587
