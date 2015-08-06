from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url('', include('django_comments.urls')),
)
