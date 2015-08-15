from django.conf.urls import patterns, url
from quizzes import views

urlpatterns = patterns('',
		url(r'^$', views.index, name="index"),
		url(r'^showResult/$', views.showResult, name="showResult"),
		#url(r'^scoreboard/$', views.scoreboard, name="scoreboard"),

		url(r'^quiz/(?P<quizShortName>[a-zA-Z0-9]+)/$', views.takeQuiz,
			name="takeQuiz"),
		url(r'^quiz/(?P<quizShortName>[a-zA-Z0-9]+)/submit/$', views.submitQuiz,
			name="submitQuiz"),
		url(r'^lesson/(?P<quizShortName>[a-zA-Z0-9]+)/$', views.lesson,
			name="lesson"),
		)
