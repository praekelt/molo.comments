from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from molo.commenting.models import MoloComment


class CommentingAdminTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            'admin', 'admin@example.org', 'admin')
        self.content_type = ContentType.objects.get_for_model(self.user)
        self.client = Client()
        self.client.login(username='admin', password='admin')

    def mk_comment(self, comment):
        return MoloComment.objects.create(
            content_type=self.content_type,
            object_pk=self.user.pk,
            content_object=self.user,
            site=Site.objects.get_current(),
            user=self.user,
            comment=comment,
            submit_date=datetime.now())

    def test_reply_link_on_comment(self):
        '''Every root comment should have the (reply) text that has a link to
        the reply view for that comment.'''
        comment = self.mk_comment('comment')
        print comment
        changelist = self.client.get(
            reverse('admin:commenting_molocomment_changelist'))
        print changelist

    def test_nested_replies(self):
        '''Replies to comments should be indented and ordered right under
        the parent comment.'''
        comment = self.mk_comment('comment')
        reply = self.mk_comment('reply')
        reply.parent = comment
        reply.save()
        print comment, reply
        changelist = self.client.get(
            reverse('admin:commenting_molocomment_changelist'))
        print changelist

    def test_comments_reverse_chronological_order(self):
        '''The admin changelist view should display comments in reverse
        chronological order.'''
        comment1 = self.mk_comment('comment1')
        comment2 = self.mk_comment('comment2')
        comment3 = self.mk_comment('comment3')
        print comment1, comment2, comment3
        changelist = self.client.get(
            reverse('admin:commenting_molocomment_changelist'))
        print changelist

    def test_reply_to_comment_view(self):
        '''A get request on the comment reply view should return a form that
        allows the user to make a comment in reply to another comment.'''
        comment = self.mk_comment('comment')
        print comment
        formview = self.client.get(
            reverse('admin:commenting_molocomment_reply', kwargs={
                'parent': comment,
            }))
        print formview

    def test_reply_to_comment(self):
        '''A valid form should create a new comment that is a reply to an
        existing comment.'''
        comment = self.mk_comment('comment')
        print comment
        response = self.client.post(
            reverse('admin:commenting_molocomment_reply', kwargs={
                'parent': comment,
            }), data={})
        print response
