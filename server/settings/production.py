"""
Django settings for www project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from .base import *


DEBUG = False

ALLOWED_HOSTS = [
    'primalmahjong.club',
    'primal-mahjong-website.herokuapp.com'
]


# COOKIES
# Recommended by `manage.py check --deploy`
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'


# Rollbar

if env('ROLLBAR_TOKEN') != '':
    ROLLBAR = {
        'access_token': env('ROLLBAR_TOKEN'),
        'environment': 'production',
        'root': BASE_DIR,
    }

    import rollbar

    rollbar.init(**ROLLBAR)
