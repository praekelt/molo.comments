from django import forms
from django.db import OperationalError
from django.utils.translation import ugettext_lazy as _
from django_comments.forms import CommentForm
from molo.commenting.models import MoloComment, CannedResponse


class ReplyCommentForm(CommentForm):
    """
    Overriding to remove dupe comment check
    """
    def get_comment_object(self):
        """
        Return a new (unsaved) comment object based on the information in this
        form. Assumes that the form is already validated and will throw a
        ValueError if not.

        Does not set any of the fields that would come from a Request object
        (i.e. ``user`` or ``ip_address``).
        """
        if not self.is_valid():
            raise ValueError("get_comment_object may only be called on valid forms")

        CommentModel = self.get_comment_model()
        new = CommentModel(**self.get_comment_create_data())

        return new


class MoloCommentForm(CommentForm):
    email = forms.EmailField(label=_("Email address"), required=False)
    parent = forms.ModelChoiceField(
        queryset=MoloComment.objects.all(),
        required=False, widget=forms.HiddenInput)

    def get_comment_model(self):
        # Use our custom comment model instead of the built-in one.
        return MoloComment

    def get_comment_create_data(self):
        # Use the data of the superclass, and add in the parent field field
        data = super(MoloCommentForm, self).get_comment_create_data()
        data['parent'] = self.cleaned_data['parent']
        return data


def get_canned_choices():
    canned_choices = [('', '---------')]
    try:
        canned_choices += ([(canned.response, canned.response_header) for canned in CannedResponse.objects.all()])
    except OperationalError:
        canned_choices = []

    return canned_choices


class MoloCommentReplyForm(ReplyCommentForm):
    parent = forms.ModelChoiceField(
        queryset=MoloComment.objects.all(), widget=forms.HiddenInput,
        required=False)
    email = forms.EmailField(
        label=_("Email address"), required=False, widget=forms.HiddenInput)
    url = forms.URLField(
        label=_("URL"), required=False, widget=forms.HiddenInput)
    name = forms.CharField(
        label=_("Name"), required=False, widget=forms.HiddenInput)
    honeypot = forms.CharField(
        required=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        parent = MoloComment.objects.get(pk=kwargs.pop('parent'))
        super(MoloCommentReplyForm, self).__init__(parent.content_object, *args, **kwargs)
        self.fields['canned_select'] = forms.ChoiceField(choices=get_canned_choices(),
                                                         label="Or add a Canned response", required=False)
