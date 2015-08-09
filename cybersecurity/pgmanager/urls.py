from django.conf.urls import patterns, url
from pgmanager import views

urlpatterns = patterns('',
		url(r'^startInstance/$', views.startInstance, name="startInstance"),
		url(r'^scoreboard/$', views.scoreboard, name="scoreboard"),
		url(r'^registerScore/$', views.registerScore, name="registerScore"),
		url(r'^$', views.index, name="index"),
		)
