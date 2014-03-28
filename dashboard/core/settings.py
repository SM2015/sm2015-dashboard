# coding: utf-8

from os.path import dirname, abspath, join
import os
import logging
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

def get_local_file(path):
    return (lambda *x: abspath(join(dirname(path), *x)))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!t2d9^+z18^85a7dw@)q)6a-6)z!fiuska#vr$xktn&f(p+*^x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'south',
    'core',
    'website',
    'tables',
    'map',
    'countries',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'sm2015_dashboard',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'
LANGUAGES = (
    ('en', u'English'),
    ('es', u'Spanish')
)
LOCALE_PATHS = (
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'locale'),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

FORMAT_MODULE_PATH = 'core.formats'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/tmp/dashboard.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },  
        'request_handler': {
                'level':'INFO',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': '/tmp/dashboard_request.log',
                'maxBytes': 1024*1024*5, # 5 MB
                'backupCount': 5,
                'formatter':'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'django.request': { # Stop SQL debug from logging to main logger
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': False
        },
    }
}


TEMPLATE_DIRS = (
     os.path.join( os.path.dirname( os.path.dirname( __file__ ) ), 'templates' ),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'core.template_processor.language.lang',
    'core.template_processor.country.countries',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')
MEDIA_URL = "/media/"

BASE_URL = "http://localhost:8000"

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nomadness.travel@gmail.com'
EMAIL_HOST_PASSWORD = '#n0m4dN3SS#'
EMAIL_PORT = 587

DEFAULT_FROM_NAME = "Dashboard"
DEFAULT_FROM_EMAIL = "noreply@dashboard.com"
DEFAULT_EMAIL_REGISTER_SUBJECT = "Dashboard - Registration Confirmation"
DEFAULT_EMAIL_FORGOT_PASSWORD_SUBJECT = "Dashboard - Forgot your password?"

LOGIN_URL = '/user/login/'
