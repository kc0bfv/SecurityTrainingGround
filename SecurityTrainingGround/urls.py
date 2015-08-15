from django.conf.urls import patterns, include, url

from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

from SecurityTrainingGround import views

from usermanagement import views as umviews
from pgmanager import views as pgviews

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SecurityTrainingGround.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"),
		url(r'^scoreboard/$', views.scoreboard, name="scoreboard"),

    url(r'^admin/', include(admin.site.urls)),

		url(r'^login/', login),
		url(r'^logout/', logout),

		url(r'^users/', include('usermanagement.urls',
			namespace="usermanagement")),

		url(r'^quizzes/', include('quizzes.urls', namespace="quizzes")),

		# Needs to be last for pattern matching
		url(r'^pgmanager/', include('pgmanager.urls', namespace="pgmanager")),
	)
