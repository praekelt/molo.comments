import datetime
from django_comments.models import Comment
from django_comments.models import CommentFlag
from django.dispatch import receiver
from django_comments.signals import comment_was_flagged
from django.conf import settings
from django_comments.moderation import CommentModerator, moderator
from molo.core.models import ArticlePage

from mptt.models import MPTTModel, TreeForeignKey


class MoloComment(MPTTModel, Comment):
    """
    Threaded comments - Add support for the parent comment store
    and MPTT traversal
    """

    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children')

    class MPTTMeta:
        # comments on one level will be ordered by date of creation
        order_insertion_by = ['submit_date']

    class Meta:
        app_label = 'commenting'
        ordering = ['-submit_date', 'tree_id', 'lft']

    def flag_count(self, flag):
        return self.flags.filter(flag=flag).count()


class ArticleModerator(CommentModerator):
    def allow(self, comment, content_object, request):
        commenting_state = getattr(content_object, 'commenting_state')
        if (commenting_state != 'open'):
            # Allow commenting between specified hours
            if (commenting_state == 'timestamped'):
                open_comments = getattr(content_object, 'open_commenting')
                close_comments = getattr(content_object, 'close_commenting')
                now = datetime.now().time()
                return open_comments < now < close_comments
            if (commenting_state == 'closed'):
                # Allow automated reopening of commenting at a specified time
                reopen_comments = getattr(content_object, 'reopen_commenting')
                if (reopen_comments):
                    now = datetime.now().time()
                    if reopen_comments < now:
                        content_object.commenting_state = 'open'
                        return True
            return False
        return True


moderator.register(ArticlePage, ArticleModerator)


@receiver(comment_was_flagged, sender=MoloComment)
def remove_comment_if_flag_limit(sender, comment, flag, created, **kwargs):
    # Auto removal is off by default
    try:
        threshold_count = settings.COMMENTS_FLAG_THRESHHOLD
    except AttributeError:
        return

    if flag.flag != CommentFlag.SUGGEST_REMOVAL:
        return
    # Don't remove comments that have been approved by a moderator
    if (comment.flag_count(CommentFlag.MODERATOR_APPROVAL) > 0):
        return

    if (comment.flag_count(CommentFlag.SUGGEST_REMOVAL) >= threshold_count):
        comment.is_removed = True
        comment.save()
