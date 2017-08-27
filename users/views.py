from django.shortcuts import render
from .models import User

def profile(request):

    template = "user/profile.html"

    user = User.objects.get(id=user_id)

    context = {"user": user}

    return render(request, template, context)