from decimal import Decimal, ROUND_UP

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from quizzes.models import Quiz, Question, Answer, QuizScore, ScoreboardEntry

def buildIndexComponents(request):
	return {"latest_quiz_list": Quiz.objects.all().order_by("id"),
			"scoreboard": ScoreboardEntry.objects.all()}

def buildScoreboardComponents(request):
	return {"scoreboard": ScoreboardEntry.objects.all()}

@login_required() # TODO: this doesn't check for disabled accounts.is that ok?
def index(request):
	context = buildScoreboardComponents(request)
	context.update(buildIndexComponents(request))
	return render(request, "quizzes/index.html", context)

def scoreboard(request):
	context = buildScoreboardComponents(request)
	return render(request, "quizzes/scoreboard.html", context)

@login_required()
def showResult(request):
	context = {"result_text": "Your score was: " + request.user.first_name}
	return render(request, "quizzes/showResult.html", context)

@login_required()
def takeQuiz(request, quizShortName):
	quiz = get_object_or_404(Quiz, shortname=quizShortName)
	return render(request, "quizzes/takequiz.html", {"quiz": quiz})

@login_required()
def lesson(request, quizShortName):
	quiz = get_object_or_404(Quiz, shortname=quizShortName)
	return render(request, "quizzes/lesson.html", {"quiz": quiz})

@login_required()
def submitQuiz(request, quizShortName):

	def correctTest(question):
		return (int(request.POST[str(question.id)]) == 
				int(question.answer_set.filter(correct=True)[0].id))

	def updateScoreboard(user):
		try:
			entry = ScoreboardEntry.objects.get(user=user)
		except ScoreboardEntry.DoesNotExist:
			entry = ScoreboardEntry(user=user, score=0)
		entry.score = 0
		for quiz in Quiz.objects.all():
			try:
				quizScore = QuizScore.objects.get(user=user, quiz=quiz)
			except QuizScore.DoesNotExist:
				pass
			else:
				entry.score += quizScore.score
		entry.save()

	quiz = get_object_or_404(Quiz, shortname=quizShortName)

	try:
		selectedAnswers = [correctTest(ques) for ques in quiz.question_set.all()]
	except KeyError:
		return render(request, "quizzes/takequiz.html",
			{"quiz": quiz, "error_message": "Error selecting options"})

	correctAnswers = Decimal(sum(1 for i in selectedAnswers if i))
	score = correctAnswers/len(selectedAnswers)*100
	score = score.quantize(Decimal('.01'), rounding=ROUND_UP)

	# Try to grab the user's existing score on this quiz
	try:
		quizScore = QuizScore.objects.get(user=request.user, quiz=quiz)
	except QuizScore.DoesNotExist:
		quizScore = QuizScore(quiz=quiz, user=request.user, score=0)
	
	# Store the best score
	oldScore = quizScore.score
	if score > quizScore.score:
		quizScore.score = score
		quizScore.save()

	# Build a results string
	if oldScore == score:
		message = "{0}.  You tied your high score.".format(score)
	elif oldScore > score:
		message = "{0}.  High score: {1}".format(score, quizScore.score)
	else:
		message = "{0}. A new high score!".format(score)
		updateScoreboard(request.user)
	request.user.first_name = message
	request.user.save()


	return HttpResponseRedirect(reverse("quizzes:showResult"))

def createUser(request):
	return render(request, "registration/createuser.html")

def submitCreateUser(request):
	username = request.POST["username"]
	password = request.POST["password"]
	favoriteFood = request.POST["favoritefood"]

	if User.objects.filter(username=username):
		return render(request, "registration/createuser.html",
				{"error_message": "Username already exists."})

	# User didn't already exist
	user = User.objects.create_user(username, favoriteFood, password)
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user) # TODO: doesn't check for disabled account
		return HttpResponseRedirect(reverse("quizzes:index"))
	else:
		return render(request, "registration/createuser.html",
				{"error_message": "Error authenticating new account."})
