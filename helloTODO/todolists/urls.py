from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
 
urlpatterns = patterns(
    '',
    url(r'^todolists/$', views.TODOListList.as_view()),
    url(r'^todolists/(?P<pk>[0-9]+)/$', views.TODOListDetail.as_view()),
    url(r'^task/$', views.TaskList.as_view()),
    url(r'^task/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
    url(r'^comment/$', views.CommentList.as_view()),
    url(r'^comment/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
)
 
urlpatterns = format_suffix_patterns(urlpatterns)