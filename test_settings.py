from .base import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + (
    'django_comments',
)

COMMENTS_APP = 'molo.commenting'
SITE_ID = 1
