"""
Django settings for pur_beurre project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("BASE_DIR :: {}".format(BASE_DIR))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^+%82556f9ka=e3q!z67#fxr1br1y*ds80)@+7=&u^*nr*hb@('
if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = []
# SECURITY WARNING: don't run with debug turned on in production!
if 'DEPLOY_ENVIRON' in os.environ and os.environ['DEPLOY_ENVIRON'] == 'PRODUCTION':
    if 'FORCE_DEBUG' in os.environ and os.environ['FORCE_DEBUG'] == 'YES':
        DEBUG = True
    else:
        DEBUG = False
    ALLOWED_HOSTS = ['15.237.65.43', 'www.lemulotfou.com', 'lemulotfou.com']
else: # FORCER LE DEBUG EN PRODUCTION
    if 'FORCE_DEBUG' in os.environ and os.environ['FORCE_DEBUG'] == 'NO':
        DEBUG = False
    else:
        DEBUG = True
    ALLOWED_HOSTS = ['127.0.0.1']

if 'DEPLOY_ENVIRON' in os.environ:
    print('DEPLOY_ENVIRON = {}'.format(os.environ and os.environ['DEPLOY_ENVIRON']))
if 'FORCE_DEBUG' in os.environ:
    print('FORCE_DEBUG = {}'.format(os.environ and os.environ['FORCE_DEBUG']))
print('ALLOWED_HOSTS :{}'.format( ",".join(ALLOWED_HOSTS) ))
print('len secret key :{}'.format(len(SECRET_KEY)))
print('DEBUG :{}'.format(DEBUG))

# Application definition

INSTALLED_APPS = [
    'product.apps.ProductConfig',
    'user.apps.UserConfig',
    'substitute.apps.SubstituteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
#    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'pur_beurre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pur_beurre.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'NAME': 'purbeurre',
        'PASSWORD': 'my00pass',
        'HOST': '127.0.0.1',
        'PORT': 5432,
        'TEST': {
                    'NAME': 'test_postgres2',
                },
    }

}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

INTERNAL_IPS = ['127.0.0.1']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

if 'DEPLOY_ENVIRON' in os.environ and os.environ['DEPLOY_ENVIRON'] == 'PRODUCTION':
#    STATIC_ROOT = os.path.join(BASE_DIR, 'dumps')
#    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = 'default_access_key_id'
    AWS_SECRET_ACCESS_KEY = 'default_secret_access_key'
    AWS_STORAGE_BUCKET_NAME = 'default_storage_bucket_name'

    if 'AWS_ACCESS_KEY_ID' in os.environ :
        AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    if 'AWS_SECRET_ACCESS_KEY' in os.environ :
        AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    if 'AWS_STORAGE_BUCKET_NAME' in os.environ :
        AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_REGION_NAME='eu-west-3'

    print('AWS_ACCESS_KEY_ID :{}'.format( AWS_ACCESS_KEY_ID ))
    print('AWS_SECRET_ACCESS_KEY :{}'.format( AWS_SECRET_ACCESS_KEY ))
    print('AWS_STORAGE_BUCKET_NAME :{}'.format( AWS_STORAGE_BUCKET_NAME ))
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

# awesome_website/settings.py
LOGIN_REDIRECT_URL = "dashboard"
# AUTH_USER_MODEL = 'user.CustomUser'
AUTHENTICATION_BACKENDS = ['user.emailbackend.EmailBackend']
