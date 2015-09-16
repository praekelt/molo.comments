from .base import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + (
    'mptt',
    'django_comments',
    'django.contrib.sites',
)

COMMENTS_APP = 'molo.commenting'
COMMENTS_FLAG_THRESHHOLD = 1
SITE_ID = 1
