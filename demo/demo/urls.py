from django.conf.urls import patterns, include, url

from django.contrib import admin
from demo.views import demo
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/',demo),
    # url(r'^demo1/$', demo.views.method_splitter, {'GET': demo.views.some_page_get, 'POST': demo.views.some_page_post}),
)
