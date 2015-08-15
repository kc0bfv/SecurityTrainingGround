from django.conf.urls import patterns, url
from usermanagement import views

urlpatterns = patterns('',
		url(r'^create/$', views.createUser, name="createUser"),
		url(r'^submit/$', views.submitCreateUser, name="submitCreateUser"),
		)
