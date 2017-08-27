from django.shortcuts import render
from django.http import HttpResponse
from .models import Step, Exercise
from django.shortcuts import render


def step_list(request):
    template = "steps/main.html"

    steps = Step.objects.all()
    context = {'steps': steps}

    return render(request, template, context)


def exercise_detail(request, step_id, exercise_id):
    template = "steps/exercise.html"

    exercise = Exercise.objects.get(step_id=step_id, id= exercise_id)

    context = {"exercise": exercise}

    return render(request, template, context)