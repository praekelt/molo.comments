from .base import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + (
    'threadedcomments',
    'django_comments',
    'django.contrib.sites',
)

COMMENTS_APP = 'threadedcomments'
