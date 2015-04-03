from django.conf.urls import patterns, include, url
from django.contrib import admin

from common.views import Index

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='index'),
    # Examples:
    # url(r'^$', 'nthucourses.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
