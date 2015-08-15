"""
Django settings for SecurityTrainingGround project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from SecurityTrainingGround.configfile import CONFIG_FILE

import json
config = json.load(open(os.path.expanduser(CONFIG_FILE)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=config["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
if len(config["prod_server"]) > 0 and (
		config["prod_server"][0] == 'y' or config["prod_server"][0] == 'Y'
		):
	DEBUG = False
else:
	DEBUG = True

TEMPLATE_DEBUG = True


# TODO: put this in the settings file maybe
#ALLOWED_HOSTS = ['.notmet.net', '192.168.0.47', 'codejamsecurity.servegame.org', 'codejam.servegame.org']
ALLOWED_HOSTS = [config["prod_domain"]]


# Application definition

INSTALLED_APPS = (
		'pgmanager',
		'usermanagement',
		'quizzes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SecurityTrainingGround.urls'

WSGI_APPLICATION = 'SecurityTrainingGround.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
		#'mysqlshell': {
		#	'ENGINE': 'django.db.backends.mysql',
		#	'NAME': '',
		#	'USER': '',
		#	'PASSWORD': '',
		#	'HOST': '',
		#	'PORT': '',
		#},
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static") ]

# Login information
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'


