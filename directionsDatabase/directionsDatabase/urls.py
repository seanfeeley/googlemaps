from django.conf.urls import patterns, include, url
from django.contrib import admin


from directionsDatabase import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.map, name='map'),
    url(r'^admin/', include(admin.site.urls)),
)