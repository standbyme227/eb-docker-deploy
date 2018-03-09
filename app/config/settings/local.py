from .base import *

DEBUG = True

# secrets = json.loads(open(SECRETS_LOCAL, 'rt').read())
SECRET_KEY = ''
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.local.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}