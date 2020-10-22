from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

# Quizzes

def quiz_index(request):
    profile = request.user.profile
    qzs = profile.quizzes.all().order_by("-created_on")
    return render(request, "quiz_index.html", {"qzs": qzs})


@login_required
def create_quiz(request):
    if request.method == "POST":
        quiz_form = QuizForm(request.POST)
        if quiz_form.is_valid():
            form = quiz_form.save(commit=False)
            form.created_by = request.user.profile
            form.save()
            messages.error(request, "Created New Quiz", extra_tags="alert")
            return redirect("quiz_index")    
    else:
        quiz_form = QuizForm()
    return render(request, "create_quiz.html", {"quiz_form": quiz_form})


@login_required
def quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    profile = request.user.profile
    return render(request, "quiz.html", {"quiz": quiz, "profile": profile})


@login_required
def delete_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    profile = request.user.profile
    if quiz.created_by == profile or profile.staff_access:
        quiz.delete()
        messages.error(
            request, f"Deleted {quiz}", extra_tags="alert"
        )
        return redirect(reverse('quiz_index'))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def edit_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    profile = request.user.profile
    if quiz.created_by == profile or profile.staff_access:
        if request.method == "POST":
            quiz_form = QuizForm(request.POST, instance=quiz)
            if quiz_form.is_valid():
                form = quiz_form.save(commit=False)
                form.save()
                messages.error(request, f"Edited {quiz}", extra_tags="alert")
                return redirect("quiz", quiz.pk)    
        else:
            quiz_form = QuizForm(instance=quiz)
            return render(request, "edit_quiz.html", {"quiz_form": quiz_form, "quiz": quiz})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def add_question_to_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    profile = request.user.profile
    if quiz.created_by == profile or profile.staff_access:
        if request.method == "POST":
            question_form = AddQuestionForm(request.POST)
            if question_form.is_valid():
                form = question_form.save(commit=False)
                form.quiz = quiz
                form.save()
                messages.error(request, f"Edited {quiz}", extra_tags="alert")
                return redirect("quiz", quiz.pk)    
        else:
            question_form = AddQuestionForm()
            return render(request, "add_question_to_quiz.html", {"question_form": question_form, "quiz": quiz})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")