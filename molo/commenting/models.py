from django_comments.models import Comment
from django.dispatch import receiver
from django_comments.signals import comment_was_flagged

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
        
@receiver(comment_was_flagged, sender=MoloComment)
def remove_comment_if_flag_limit(sender, comment, flag, created, **kwargs):
    if (comment.flags.count() >= 3):
        comment.is_removed = True
        comment.save()
