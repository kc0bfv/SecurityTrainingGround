from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
	title = models.CharField(max_length=256)
	shortname = models.CharField(max_length=10)
	lessonContent = models.TextField()

	def __str__(self):
		return self.title + "(" + self.shortname + ")"

class Question(models.Model):
	quiz = models.ForeignKey(Quiz) #Which quiz does the question occur in?
	question = models.TextField()
	pointValue = models.IntegerField(default=1)

	def __str__(self):
		return self.question + " ({0} points)".format(self.pointValue)

class Answer(models.Model):
	question = models.ForeignKey(Question) #The question the answer belongs to
	answer = models.TextField()
	correct = models.BooleanField() #True if this is the correct answer

	def __str__(self):
		return self.answer + ("(correct)" if self.correct else "(incorrect)")

class QuizScore(models.Model):
	quiz = models.ForeignKey(Quiz) # The quiz this score goes with
	user = models.ForeignKey(User) # The user this score goes with
	score = models.DecimalField(max_digits=5, decimal_places=2) # The score

class ScoreboardEntry(models.Model):
	user = models.ForeignKey(User)
	score = models.DecimalField(max_digits=6, decimal_places=0)
	time = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-score','time']

# Right now, favoriteFood and resultMessage are implemented with the User email address and first_name fields, respectively.  This works fine for my simple case, but at some point in the future, something more like this might be necessary
#class UserSupplement(models.Model):
#	user = models.OneToOneField(User)
#	favoriteFood = models.CharField(max_length=256)
#	resultMessage = models.CharField(max_length=256)
