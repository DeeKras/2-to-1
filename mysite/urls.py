from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from profiles import views
from mysite import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),

    url(r'^$', 'profiles.views.home', name='home'),

    url(r'^advocate/create', 'profiles.views.registration', name='advocate_create'),
    url(r'^login', 'profiles.views.login', name='login'),
    url(r'^logout', 'profiles.views.logout', name='logout'),

    url(r'^advocate/edit/(?P<pk>\d+)$', views.AdvocateUpdate.as_view(), name='advocate_edit'),
    url(r'^advocate$', 'profiles.views.advocate_homepage', name='advocate_homepage'),

    url(r'^single/create', views.SingleCreate.as_view(), name='single_create'),
    url(r'^single/edit/(?P<pk>\d+)$', views.SingleUpdate.as_view(), name='single_edit'),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



