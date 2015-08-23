from django.contrib import admin
from quizzes.models import Quiz, Question, Answer, QuizScore, ScoreboardEntry

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

class QuizScoreAdmin(admin.ModelAdmin):
	pass

class ScoreboardEntryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizScore, QuizScoreAdmin)
admin.site.register(ScoreboardEntry, ScoreboardEntryAdmin)
