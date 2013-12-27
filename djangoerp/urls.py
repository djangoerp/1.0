from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

from base import views, users_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoerp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$',  login,{'template_name': 'login.html'}),
    (r'^logout/$', logout,{'next_page': '/'}),
    url(r'^users/$', users_views.user_list, name='user_list'),
    url('^users/(?P<id>\d+)/$', 'base.users_views.user_detail'),

)
