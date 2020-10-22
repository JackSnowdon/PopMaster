from django.urls import path
from .views import *

urlpatterns = [
    path('quiz_index/', quiz_index, name="quiz_index"),
    path('create_quiz/', create_quiz, name="create_quiz"),
]