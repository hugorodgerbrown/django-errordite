"""
Simplest possible settings.py for use in running django-related unit tests.

This settings file would be completely useless for running a project, however
it has enough in it to be able to run the django unit test runner, and to spin
up django.contrib.auth users.

In order for the tests to run, you will need to set the following environment
variable: ERRORDITE_TOKEN.

Please see online documentation for more details.
"""
from os import environ as env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'delme'
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'test_app',
)

ERRORDITE_TOKEN = env.get('ERRORDITE_TOKEN', None)
if ERRORDITE_TOKEN is None:
    raise Exception("You must set the ERRORDITE_TOKEN environment "
                    "variable if you wish to run the tests.")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'django_errordite': {
            'level': 'DEBUG',
            'class': 'django_errordite.DjangoErrorditeHandler',
            'token': ERRORDITE_TOKEN,
            'formatter': 'simple'
        },
    },
    'loggers': {
        'test': {
            'handlers': ['django_errordite'],
            'propagate': False,
            'level': 'DEBUG',
        },
    }
}

SECRET_KEY = "something really, really hard to guess goes here."
