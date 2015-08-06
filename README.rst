Molo Comments
=============

.. image:: https://travis-ci.org/praekelt/molo.comments.svg?branch=develop
    :target: https://travis-ci.org/praekelt/molo.comments
    :alt: Continuous Integration

.. image:: https://coveralls.io/repos/praekelt/molo.comments/badge.png?branch=develop
    :target: https://coveralls.io/r/praekelt/molo.comments?branch=develop
    :alt: Code Coverage

Installation::

   pip install molo.comments


Django setup::

   INSTALLED_APPS = INSTALLED_APPS + (
       'django_comments',
       'mptt',
       'molo.comments',
       'django.contrib.sites',
   )

   COMMENTS_APP = 'molo.comments'
   SITE_ID = 1

In your urls.py::

   urlpatterns += patterns('',
       url(r'^comments/', include('molo.comments.urls')),
   )
