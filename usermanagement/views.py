from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from pgmanager.models import BestScore
from quizzes.models import ScoreboardEntry

def createUser(request):
	return render(request, "usermanagement/createuser.html")

def submitCreateUser(request):
	#TODO: what happens if someone doesn't submit these fields in their post?
	username = request.POST["username"]
	password = request.POST["password"]
	favoriteFood = request.POST["favoritefood"]

	if User.objects.filter(username=username):
		return render(request, "usermanagement/createuser.html",
				{"error_message": "Username already exists."})

	# User didn't already exist
	user = User.objects.create_user(username, favoriteFood, password)
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user) # TODO: doesn't check for disabled account
		return HttpResponseRedirect(reverse("pgmanager:index"))
	else:
		return render(request, "usermanagement/createuser.html",
				{"error_message": "Error authenticating new account."})
