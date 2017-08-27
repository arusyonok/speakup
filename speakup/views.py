from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'landing.html'

    return render(request, template)