from django.conf.urls import url, patterns

from common import views


urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^status/$', views.Status.as_view(), name='status'),
)
