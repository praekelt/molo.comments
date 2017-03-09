from .base import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + [
    'django_comments',
    'notifications',
]

COMMENTS_APP = 'molo.commenting'
SITE_ID = 1
