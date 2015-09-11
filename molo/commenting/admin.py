from django.contrib import admin

from molo.commenting.models import MoloComment
from django_comments.models import CommentFlag
from django_comments.admin import CommentsAdmin
from django.core.urlresolvers import reverse



class MoloCommentAdmin(CommentsAdmin):
    list_display = ('comment', 'content_object', '_user', 'is_removed', 'is_reported', 'submit_date')
    
    def is_reported(self, obj):
        if (obj.flags.count()>0):
            return True
        return False
    is_reported.admin_order_field = 'is_reported'
    is_reported.boolean = True
    
    def _user(self, obj):
        url = reverse('admin:auth_user_change', args=(obj.user.id,))
        return '<a href="?user=%s">%s</a>' % (
            obj.user.id,
            obj.user
        ) + ' (<a href="%s">edit</a>)' % url
    _user.allow_tags = True
    _user.short_description = 'User'


admin.site.register(MoloComment, MoloCommentAdmin)
admin.site.register(CommentFlag)
