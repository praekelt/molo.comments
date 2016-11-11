CHANGELOG
=========

1.0.3
-----
- Remove a duplicate line in migration

1.0.2
-----
- Fix a bug in permissions migration

1.0.1
-----
- Add commenting permissions to groups

1.0.0
-----
- Add BEM template naming convention
- Add namespace to commenting URLs in the temolates
- Remove `url(r'', include('django_comments.urls'))` from commenting URLs
Note: If you are using this release you need to add the `url(r'', include('django_comments.urls'))` to your app's urls.py

0.5.4
-----
- Pin pytest to 2.9
- Pin django-mptt to 0.8.5

0.5.3
-----
- Change extended template for reply.html

0.5.2
-----
- Convert unicode to encoded text for article title

0.5.1
-----
- Return None if there is no user

0.5.0
-----
- Added Comments view to Wagtail Admin

0.4.2
-----
- add missing migration
- only allow admin users to post duplicate comments

0.4.1
-----
- Removed `{% load url from future %}`
- Use user's alias when posting a comment

0.4.0
-----
- Now compatible with Django 1.9 (removed model import in __init__.py)

0.3.2
-----
- Added canned response.

0.3.1
-----
- Order comments from newest to oldest unless they are replies.

0.3
---
- Add canned responses

0.2.9
-----
- Add support for replying to comments from the admin interface.
