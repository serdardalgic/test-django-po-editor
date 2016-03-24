from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from . import views

admin.autodiscover()


urlpatterns = i18n_patterns('',
                            url(r'^app1/', include('app1.urls')),
                            url(r'^app2/', include('app2.urls')),
                            url(r'^admin', include(admin.site.urls)),
                            url(r'^$', views.index, name='index'),
                            )
