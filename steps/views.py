from django.shortcuts import render
from django.http import HttpResponse
from .models import Exercise
from django.shortcuts import render


def exercise_list(request):
    template = "steps/exerciselist.html"

    exercises = Exercise.objects.all()
    context = {'steps': exercises}

    return render(request, template, context)