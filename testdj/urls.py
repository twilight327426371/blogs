# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from testdj import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
    url(r'^blog/list$', views.blog_list),
    url(r'^blog/form$', views.blog_form),
    url(r'^blog/delete$', views.blog_del),
    url(r'^blog/view$', views.blog_view),
    url(r'^blog/edit$', views.blog_edit),
]
