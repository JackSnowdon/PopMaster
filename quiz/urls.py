from django.urls import path
from .views import *

urlpatterns = [
    path('quiz_index/', quiz_index, name="quiz_index"),
    path('create_quiz/', create_quiz, name="create_quiz"),
    path(r'quiz/<int:pk>/', quiz, name="quiz"),
    path(r'delete_quiz/<int:pk>/', delete_quiz, name="delete_quiz"),
    path(r'edit_quiz/<int:pk>/', edit_quiz, name="edit_quiz"),
    
]