from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EC2Instance(models.Model):
	instanceID = models.CharField(max_length=50)
	user = models.ForeignKey(User)
	startTime = models.DateTimeField(auto_now_add=True)
	score = models.IntegerField(default=0)
	ip = models.CharField(max_length=50, default="0.0.0.0")

class BestScore(models.Model):
	user = models.ForeignKey(User)
	score = models.IntegerField(default=0)
	time = models.DateTimeField(auto_now=True)
