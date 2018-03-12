from .base import *

DEBUG =True

secrets = json.loads(open(SECRETS_DEV, 'rt').read())

ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.dev.application'

set_config(secrets, module_name=__name__, start=True)
# print(getattr(sys.modules[__name__],'DATABASES'))
# DATABASES = secrets['DATABASES']

INSTALLED_APPS +=[
    'django_extensions',
]

DEFAULT_FILE_STORAGE = 'config.storage.DeFaultFilesStorage'
STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'