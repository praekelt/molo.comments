CHANGELOG
=========
10.0.3
~~~~~~
- Fix Admin comment list pagination with date filters

10.0.2
~~~~~~
- Update MoloComment signal handler add attribute checks to update wagtail site

10.0.0
~~~~~~
- Support Django 2.2+

8.0.1
~~~~~
- Deploy on Python 3 build

8.0.0
~~~~~
- Upgrade to wagtail 2

7.0.1
-----
-Fix pycodestlye errors
-Update comment edit to make only the comment text editable

7.0.0
-----
- Upgrade to molo 7

6.3.0
-----
- Fix bug in delete comments

6.2.9
-----
- Fix bug in user comments export

6.2.8
-----
- Remove settings to change commenting alias
- Return rule data if the user does not match the rules

6.2.7
-----
- Add settings to change commenting alias

6.2.6
-----
- Add methods to get user data from segmentation rule

6.2.5
-----
- Update wagtail-personalisation version

6.2.4
-----
- Enable segmentation rules to be tested without active requests

6.2.3
-----
- Fix comment admin for unicode comments on Python 2

6.2.2
-----
- Fix comment admin for unicode comments on Python 2

6.2.1
-----
- Ensure segmentation rules are marked as static

6.2.0
-----
- Add support for Python 3

6.1.1
-----
- Plugin templates refactor and cleanup

6.1.0
-----
- add support for Django 1.11

6.0.1
-----
- add is_staff filter to admin

6.0.0
-----
- Official Release of Commenting 6.0.0
- No longer supporting Django 1.9, see upgrade considerations
  https://docs.djangoproject.com/en/2.0/releases/1.10/

6.0.5-beta.1
------------
- Remove __latest__ from migration dependencies

6.0.4-beta.1
------------
- Bug Fix in Migration: Rely on Django Auth Latest migration for Django 1.10

6.0.3-beta.1
------------
- Bug Fix in Migration: Rely on Django Auth Latest

6.0.1-beta.1
------------
- upgrade to Django 1.10, molo 6x

5.2.3
-----
- Remove comment field placeholder

5.2.2
-----
- Update dependency on wagtail-personalisation to wagtail-personalisation-molo, a custom, forked version

5.2.1
-----
- Bug Fix: redirect edit user page to wagtail admin not django-admin

5.2.0
-----
- Added Comment Rules for Personalise

5.1.0
-----
- Deprecated the use of download as CSV due to timeouts. Implemented send CSV as email.

5.0.2
-----
- Bug Fix: use unicode for comments in admin

5.0.1
-----
- Update trans blocks

5.0.0
-----
- Add multi-site support

2.1.3
-----
- Add trans block on comment textarea widget form
=======

2.1.2
-----
- Add placeholder attribute on comment textarea widget form

2.1.1
-----
- Updated notifications templates user-interface for users when comments are replied to by user admin

2.1.0
-----
- Added notifications for users when comments are replied to
- Added threaded comments that allow all users to reply to comments

2.0.1
-----
- Updated templates in order to reflect styling changes in modeladmin

2.0.0
-----
- Removed dependency on wagtailmodeladmin

Backwards incompatible changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Removed use of ``wagtailmodeladmin``: use ``wagtail.contrib.modeladmin`` instead
- ``{% load wagtailmodeladmin_tags %}`` has been replaced by ``{% load modeladmin_tags %}``

NOTE: This release is not compatible with molo versions that are less than 4.0

1.0.4
-----
- Delete Comment Moderator and Expert group and recreate them again

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
