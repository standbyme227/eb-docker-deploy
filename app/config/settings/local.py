from .base import *

DEBUG = True

secrets = json.loads(open(SECRETS_LOCAL, 'rt').read())

ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.local.application'
DATABASES = secrets['DATABASES']

INSTALLED_APPS +=[
    'django_extensions',
]