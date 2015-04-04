from django.conf.urls import patterns, url

from courses import views


urlpatterns = patterns('',
    url(r'^courses/$', views.Course.as_view(), name='courses'),
)
