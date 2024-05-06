from .settings import *

DEBUG = False
ALLOWED_HOSTS = []
STATIC_ROOT = (BASE_DIR / 'static/')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
