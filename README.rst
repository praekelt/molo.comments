Molo Comments
=============

.. image:: https://travis-ci.org/praekelt/molo.comments.svg?branch=develop
    :target: https://travis-ci.org/praekelt/molo.comments
    :alt: Continuous Integration

.. image:: https://coveralls.io/repos/praekelt/molo.comments/badge.png?branch=develop
    :target: https://coveralls.io/r/praekelt/molo.comments?branch=develop
    :alt: Code Coverage

Provides code to help with comments in a project using the Molo code base.
Currently this is really just a convenience wrapper around
``django-threadedcomments``.

Installation::

   pip install molo.comments


Django setup::

   INSTALLED_APPS = (
      'threadedcomments',
      'django.contrib.comments',
   )

In your urls.py::

   urlpatterns += patterns('',
       url(r'^comments/', include('molo.comments.urls')),
   )
