from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('common.urls')),
    url(r'^', include('courses.urls')),
    # Examples:
    # url(r'^$', 'nthucourses.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
)
