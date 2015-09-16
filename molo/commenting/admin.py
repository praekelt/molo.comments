from django.contrib import admin

from molo.commenting.models import MoloComment
from django_comments.models import CommentFlag
from django_comments.admin import CommentsAdmin
from django.core.urlresolvers import reverse
from django.contrib.admin.views.main import ChangeList
from django.contrib.contenttypes.models import ContentType


class MoloCommentAdmin(CommentsAdmin):
    list_display = ('comment', 'content', '_user', 'is_removed', 'is_reported', 'submit_date')
    
    def is_reported(self, obj):
        if (obj.flags.count()>0):
            return True
        return False
    is_reported.admin_order_field = 'is_reported'
    is_reported.boolean = True
    
    def get_user_display_name(self, obj):
        if obj.name.lower().startswith('anon'):
            return obj.user.username
        return obj.name
    
    def _user(self, obj):
        url = reverse('admin:auth_user_change', args=(obj.user.id,))
        return '<a href="?user=%s">%s</a>' % (
            obj.user.id,
            self.get_user_display_name(obj)
        ) + ' (<a href="%s">edit</a>)' % url
    _user.allow_tags = True
    _user.short_description = 'User'
    
    def content(self, obj):
        return '<a href="?object_pk=%s">%s</a>' % (
            obj.object_pk,
            obj.content_object
        )
    content.allow_tags = True
    content.short_description = 'Content'

    def get_changelist(self, request):
        class ModeratorChangeList(ChangeList):
            def get_queryset(self, request):
                """
                Used by AdminModeratorMixin.moderate_view to somewhat hackishly
                limit comments to only those for the object under review, but
                only if an obj attribute is found on request (which means the
                mixin is being applied and we are not on the standard
                changelist_view).
                """
                qs = super(ModeratorChangeList, self).get_queryset(request)
                obj = getattr(request, 'obj', None)
                if obj:
                    ct = ContentType.objects.get_for_model(obj)
                    qs = qs.filter(content_type=ct, object_pk=obj.pk)
                return qs

            def get_results(self, request):
                """
                Create a content_type map to individual objects through their
                id's to avoid additional per object queries for generic
                relation lookup (used in MoloCommentAdmin.content method).
                Also create a comment_reply map to avoid additional reply
                lookups per comment object
                (used in CommentAdmin.moderator_reply method)
                """
                super(ModeratorChangeList, self).get_results(request)
                comment_ids = []
                object_pks = []

                results = list(self.result_list)
                for obj in results:
                    comment_ids.append(obj.id)
                    object_pks.append(obj.object_pk)

                ct_map = {}
                for obj in results:
                    if obj.content_type not in ct_map:
                        ct_map.setdefault(obj.content_type, {})
                        for content_obj in obj.content_type.model_class()._default_manager.filter(pk__in=object_pks):
                            ct_map[obj.content_type][content_obj.id] = content_obj
                self.model_admin.ct_map = ct_map

        return ModeratorChangeList

admin.site.register(MoloComment, MoloCommentAdmin)
admin.site.register(CommentFlag)
