from django.contrib import admin

from molo.commenting.models import MoloComment
from django_comments.models import CommentFlag
from django_comments.admin import CommentsAdmin



class MoloCommentAdmin(CommentsAdmin):
    list_display = ('comment', 'content_object', 'user', 'is_removed', 'submit_date')
    

admin.site.register(MoloComment, MoloCommentAdmin)
admin.site.register(CommentFlag)
