from .base import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + [
    'django_comments',
    'notifications',
    'wagtail_personalisation',
]

COMMENTS_APP = 'molo.commenting'
SITE_ID = 1
