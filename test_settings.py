from .base import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + (
    'mptt',
    'django_comments',
    'molo.commenting',
    'django.contrib.sites',
)

COMMENTS_APP = 'molo.commenting'
SITE_ID = 1
