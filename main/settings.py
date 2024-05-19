"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import environ
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # Django
    DJANGO_DEBUG=(bool, False),
    DOCKER_HOST_IP=(str, None),
    DJANGO_SECRET_KEY=str,
    DJANGO_MEDIA_URL=(str, '/media/'),
    DJANGO_MEDIA_ROOT=(str, os.path.join(BASE_DIR, 'media')),
    DJANGO_STATIC_URL=(str, '/static/'),
    DJANGO_STATIC_ROOT=(str, os.path.join(BASE_DIR, 'static')),
    DJANGO_ADDITIONAL_ALLOWED_HOSTS=(list, []),
    # Database
    DJANGO_DB_NAME=str,
    DJANGO_DB_USER=str,
    DJANGO_DB_PASS=str,
    DJANGO_DB_HOST=str,
    DJANGO_DB_PORT=(int, 5432),
    # Pytest (Only required when running tests)
    PYTEST_XDIST_WORKER=(str, None),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    *env('DJANGO_ADDITIONAL_ALLOWED_HOSTS'),
]
SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env('DJANGO_DEBUG')
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    # third party apps
    'rest_framework',
    'drf_spectacular',
    'django_filters',
    'rest_framework.authtoken',
    'rangefilter',

    # local apps
    'coffee',
    'order',
    'customer',
    'inventory',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env('DJANGO_DB_NAME'),
        'USER': env('DJANGO_DB_USER'),
        'PASSWORD': env('DJANGO_DB_PASS'),
        'HOST': env('DJANGO_DB_HOST'),
        'PORT': '5432',
    }
}

TESTING = any([
    arg in sys.argv for arg in [
        'test',
        'pytest',
        'py.test',
        '/usr/local/bin/pytest',
        '/usr/local/bin/py.test',
        '/usr/local/lib/python3.10/dist-packages/py/test.py',
    ]
    # Provided by pytest-xdist (If pytest is used)
]) or env('PYTEST_XDIST_WORKER') is not None

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'
STATIC_URL = "/staticfiles/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TESTING = any([
    arg in sys.argv for arg in [
        'test',
        'pytest',
        'py.test',
        '/usr/local/bin/pytest',
        '/usr/local/bin/py.test',
        '/usr/local/lib/python3.10/dist-packages/py/test.py',
    ]
    # Provided by pytest-xdist (If pytest is used)
]) or env('PYTEST_XDIST_WORKER') is not None

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'EXCEPTION_HANDLER': 'main.exception_handler.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'COFFEE',
    'DESCRIPTION': 'COFFEE API Documenation',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
