# -*- coding: utf-8 -*-
'''
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
'''

from .settings import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
#DEBUG = env.bool('DJANGO_DEBUG', default=True)
#TEMPLATES[0]['OPTIONS']['debug'] = DEBUG



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbintegra',
        'USER': 'integrauser',
        'PASSWORD': 'db_usr_integra',
        'HOST': '127.0.0.1',
    }
}