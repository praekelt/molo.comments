from import_export import resources

from molo.commenting.models import MoloComment


class MoloCommentsResource(resources.ModelResource):
    class Meta:
        model = MoloComment
        exclude = ('id', 'comment_ptr', 'content_type', 'object_pk',
                   'site', 'user', 'user_url', 'lft', 'rght',
                   'tree_id', 'level', 'ip_address', )
