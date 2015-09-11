from django.contrib import admin

from molo.commenting.models import MoloComment
from django_comments.models import CommentFlag
from django_comments.admin import CommentsAdmin



class MoloCommentAdmin(CommentsAdmin):
    list_display = ('comment', 'content_object', 'user', 'is_removed', 'is_reported', 'submit_date')
    
    def is_reported(self, obj):
        if (obj.flags.count()>0):
            return True
        return False
    is_reported.admin_order_field = 'is_reported'
    is_reported.boolean = True
    

admin.site.register(MoloComment, MoloCommentAdmin)
admin.site.register(CommentFlag)
