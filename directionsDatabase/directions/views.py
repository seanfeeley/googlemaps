from django.shortcuts import render


urlpatterns = patterns('',
    url(r'^directions/', include('directions.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
# Create your views here.
