from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from emailcontactform import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NexToU.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/', views.BasicContactView.as_view(),name='contact'),
)
