# coding: utf-8
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from sampleapp import views

urlpatterns = [
    url(r'^login/$', views.do_login),
    url(r'^job/$', views.DoTaskView.as_view()),
    url(r'^job/(?P<job_id>[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})$', views.DoTaskView.as_view()),
    url(r'^syncjob/$', views.DoSyncTaskView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
