from django.conf.urls import url
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from import_export import resources
from molo.commenting.admin import MoloCommentAdmin, CannedResponseModelAdmin
from molo.commenting.models import MoloComment, CannedResponse
from molo.commenting.views import WagtailCommentReplyView
from wagtail.wagtailcore import hooks
from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register, \
    ModelAdminGroup
from wagtailmodeladmin.views import IndexView


@hooks.register('register_admin_urls')
def register_admin_reply_url():
    return [
        url(r'comment/(?P<parent>\d+)/reply/$',
            WagtailCommentReplyView.as_view(),
            name='wagtail-molo-comment-reply'),
    ]


class CommentsResource(resources.ModelResource):
    class Meta:
        model = MoloComment
        exclude = ('id', 'comment_ptr', 'content_type', 'object_pk',
                   'site', 'user', 'user_url', 'lft', 'rght',
                   'tree_id', 'level', 'ip_address', )


class ModelAdminTemplate(IndexView):
    def post(self, request, *args, **kwargs):

        submit_date__gte = request.GET.get('submit_date__gte')
        submit_date__lt = request.GET.get('submit_date__lt')
        is_removed__exact = request.GET.get('is_removed__exact')

        filter_list = {
            'submit_date__range': (submit_date__gte,
                                   submit_date__lt) if
            submit_date__gte and submit_date__lt else None,
            'is_removed': is_removed__exact
        }

        arguments = {}

        for key, value in filter_list.items():
            if value:
                arguments[key] = value

        dataset = CommentsResource().export(
            MoloComment.objects.filter(**arguments)
        )

        response = HttpResponse(dataset.csv, content_type="csv")
        response['Content-Disposition'] = \
            'attachment; filename=comments.csv'
        return response

    def get_template_names(self):
        return 'admin/molo_admin_template.html'


class MoloCommentsModelAdmin(ModelAdmin, MoloCommentAdmin):
    model = MoloComment
    menu_label = 'Comments'
    menu_icon = 'edit'
    menu_order = 100
    index_view_class = ModelAdminTemplate
    add_to_settings_menu = False
    list_display = (
        'comment', 'moderator_reply', 'content', '_user', 'is_removed',
        'is_reported', 'reported_count', 'submit_date',)

    list_filter = ('submit_date', 'site', 'is_removed',)

    search_fields = ('comment',)

    def content(self, obj, *args, **kwargs):
        if obj.content_object and obj.parent is None:
            return (
                '<a href="/admin/pages/{0}/edit/">{1}</a>'
                .format(obj.content_object.pk, obj.content_object.title))
        return

    content.allow_tags = True
    content.short_description = ''

    def moderator_reply(self, obj):
        if obj.parent is None:
            reply_url = reverse(
                'wagtail-molo-comment-reply', args=(obj.id,))
            return '<a href="%s">Add reply</a>' % reply_url
        else:
            return ''
    moderator_reply.allow_tags = True


class MoloCannedResponsesModelAdmin(ModelAdmin, CannedResponseModelAdmin):
    model = CannedResponse
    menu_label = 'Canned Responses'
    menu_icon = 'openquote'
    menu_order = 200

    list_display = ('response_header', 'response', 'date_added')

    search_fields = ('response_header',)


class CommentingAdminGroup(ModelAdminGroup):
    menu_label = 'Commenting'
    menu_icon = 'edit'
    menu_order = 300
    items = (MoloCommentsModelAdmin, MoloCannedResponsesModelAdmin)


wagtailmodeladmin_register(CommentingAdminGroup)
