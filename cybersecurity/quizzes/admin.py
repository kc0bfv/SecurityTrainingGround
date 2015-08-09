from django.contrib import admin
from quizzes.models import Quiz, Question, Answer

class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 1

class QuestionInline(admin.TabularInline):
	model = Question
	extra = 1

class QuizAdmin(admin.ModelAdmin):
	inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['question', 'quiz']
	list_filter = ['quiz']
	inlines = [AnswerInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
