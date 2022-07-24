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


# Rollbar

if env('ROLLBAR_TOKEN') != '':
    ROLLBAR = {
        'access_token': env('ROLLBAR_TOKEN'),
        'environment': 'production',
        'branch': 'main',
        'root': BASE_DIR,
    }
