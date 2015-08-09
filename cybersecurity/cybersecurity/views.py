from django.shortcuts import render

from pgmanager.models import BestScore
from quizzes.models import ScoreboardEntry
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from pgmanager import views as pgviews
from quizzes import views as qzviews

def buildScoreboardComponents(request):
	pgscores = BestScore.objects.all()
	qzscores = ScoreboardEntry.objects.all()

	# Build a list of all users with scores
	userList = {i.user for i in pgscores}.union({i.user for i in qzscores})

	# For all those users, get both their scores and score sum
	sortableScoreList = list()
	for user in userList:
		try:
			pgscore = BestScore.objects.get(user=user).score
		except:
			pgscore = 0

		try:
			qzscore = ScoreboardEntry.objects.get(user=user).score
		except:
			qzscore = 0

		totalScore = qzscore + pgscore

		sortableScoreList.append((totalScore, {"username": user.username,
			"score": totalScore, "qzscore": qzscore, "pgscore": pgscore}))

	sortableScoreList.sort()
	sortedScoreList = [i[1] for i in sortableScoreList]

	return {"scoreboard": sortedScoreList}




def scoreboard(request):
	context = buildScoreboardComponents(request)

	return render(request, "cybersecurity/scoreboard.html", context)

@login_required()
def index(request):
	context = pgviews.buildIndexComponents(request)
	context.update(qzviews.buildIndexComponents(request))

	# Do the scoreboard last because those other ones might do a scoreboard too
	context.update(buildScoreboardComponents(request))

	return render(request, "cybersecurity/index.html", context)
