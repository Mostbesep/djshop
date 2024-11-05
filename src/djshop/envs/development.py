from .common import *


ALLOWED_HOSTS = ['*']

INSTALLED_APPS  =  [
   'daphne',
   'drf_spectacular',
] + INSTALLED_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djshop',
        'USER': 'djshop',
        'PASSWORD': '123@456',
        'HOST': 'db',
        'PORT': '5432',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        'LOCATION': 'redis://redis:6379',
    }
}

# LOGGING = {
#     'version': 1,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#         },
#     },
#     'root': {
#         'handlers': ['console'],
#     }
# }