import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from pgmanager.models import EC2Instance, BestScore
from cybersecurity.settings import CONFIG_FILE

import cybersecurity.manageEC2 as manageEC2

def buildIndexComponents(request):
	bestScore = BestScore.objects.filter(user=request.user)
	instances = EC2Instance.objects.filter(user=request.user)
	config = manageEC2.readConfig()

	context = {}

	if instances:
		instance = instances[0]

		# If we haven't tried to get the IP yet, or we've failed, try again
		if instance.ip == "0.0.0.0":
			instance.ip = manageEC2.getInstIP(instance.instanceID)
			instance.save()

		timeDelta = datetime.timedelta(hours=int(config["image_hours"]),
				minutes=int(config["image_minutes"]))
		curTime = datetime.datetime.now(datetime.timezone.utc)
		timeLeft = (timeDelta - (curTime - instance.startTime))
		niceTimeLeft = datetime.timedelta(seconds=int(timeLeft.total_seconds()))

		context["timeLeft"] = niceTimeLeft
		context["currentScore"] = instance.score
		context["IPAddr"] = instance.ip
		context["username"] = config["ami_username"]
		context["password"] = config["ami_password"]

	if bestScore:
		context["bestScore"] = bestScore[0].score
		context["bestScoreTime"] = bestScore[0].time

	return context

def buildScoreboardComponents(request):
	return {"scoreboard": BestScore.objects.all()}

@login_required()
def index(request):
	context = buildScoreboardComponents(request)
	context.update(buildIndexComponents(request))
	return render(request, "pgmanager/index.html", context)

@login_required()
def startInstance(request):
	if EC2Instance.objects.filter(user=request.user):
		# The user already has an instance started, so redirect to the index
		return HttpResponseRedirect(reverse("index"))

	else:
		# There's no existing instance, so start one up!
		config = manageEC2.readConfig()

		user_data=config["score_server_address"] + ";" + str(request.user.id) 

		instanceID = manageEC2.startInstance(user_data)

		instance = EC2Instance(instanceID=instanceID, user=request.user)

		instance.save()

		return render(request, "pgmanager/startInstance.html")

def scoreboard(request):
	context = buildScoreboardComponents(request)
	return render(request, "pgmanager/scoreboard.html", context)

@csrf_exempt
# This is not a very secure way to get the score.
# For my purposes that's ok
def registerScore(request):
	config = manageEC2.readConfig()

	validScoreLims = [int(config["image_scoremin"]), int(config["image_scoremax"])]

	try:
		userID = int(request.POST["userID"])
		score = int(request.POST["score"])
	except KeyError:	# Should happen when someone doesn't provide a POST field
		return HttpResponse("")
	except ValueError:	# Should happen when the field isn't an integer
		return HttpResponse("")

	try:
		user = User.objects.get(id=userID)
		instance = EC2Instance.objects.get(user=user)
	except: # Likely errors: django DoesNotExist, OverflowError
		return HttpResponse("")

	if score > max(validScoreLims) or score < min(validScoreLims):
		return HttpResponse("")

	instance.score=score
	instance.save()

	# If this is the best score, set it and save it
	try:
		bestScore = BestScore.objects.get(user=user)
	except: # Likely exception: django DoesNotExist
		bestScore = BestScore(user=user, score=-1)

	if score > bestScore.score:
		bestScore.score=score
		bestScore.save()

	return HttpResponse("") # Don't render anything on success or failure
