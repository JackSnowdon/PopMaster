from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

def quiz_index(request):
    profile = request.user.profile
    qzs = profile.quizzes.all().order_by("-created_on")
    return render(request, "quiz_index.html", {"qzs": qzs})


@login_required
def create_quiz(request):
    if request.method == "POST":
        quiz_form = NewQuizForm(request.POST)
        if quiz_form.is_valid():
            form = quiz_form.save(commit=False)
            form.created_by = request.user.profile
            form.save()
            messages.error(request, "Created New Quiz", extra_tags="alert")
            return redirect("quiz_index")    
    else:
        quiz_form = NewQuizForm()
    return render(request, "create_quiz.html", {"quiz_form": quiz_form})