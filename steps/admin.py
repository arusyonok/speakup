from django.contrib import admin
from .models import *


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question')


class QuestionAdmin(admin.ModelAdmin):
    fields = ['title']
    inlines = [ChoiceInline]

    list_display = ('title', 'choices', )

class StepAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'exercise_count',)

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'belongs_to','is_question','question')

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)