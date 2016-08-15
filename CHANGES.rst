CHANGELOG
=========

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
