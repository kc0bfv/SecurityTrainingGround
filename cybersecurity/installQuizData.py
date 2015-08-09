#!/usr/bin/env python3
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cybersecurity.settings")
import django
django.setup()

from quizData import quizData
from quizzes.models import Quiz, Question, Answer

for quizEntry in quizData:
	# Get the existing quiz entry if it exists, otherwise create one
	try:
		qz = Quiz.objects.get(shortname=quizEntry["shortname"])
	except Quiz.DoesNotExist:
		qz = Quiz(shortname=quizEntry["shortname"])

	qz.title = quizEntry["title"]
	with open(quizEntry["lessonContentFile"], "r") as f:
		qz.lessonContent = f.read()

	qz.save()

	# Delete any existing questions
	for quest in qz.question_set.all():
		# Delete the existing answers
		for ans in quest.answer_set.all():
			ans.delete()

		quest.delete()

	# Create the new questions
	for questEntry in quizEntry["questions"]:
		quest = qz.question_set.create(
				question=questEntry["question"], pointValue = questEntry["pointValue"])
		for ansEntry in questEntry["answers"]:
			quest.answer_set.create(
					answer=ansEntry["answer"],
					correct=(False if "correct" not in ansEntry
						else ansEntry["correct"]),
					)

