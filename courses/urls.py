from django.conf.urls import patterns, url

from courses import views


urlpatterns = patterns('',
    url(r'^$', views.Curriculum.as_view(), name='courses'),
)
