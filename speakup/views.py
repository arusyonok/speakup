from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    template = 'home.html'

    return render(request, template)