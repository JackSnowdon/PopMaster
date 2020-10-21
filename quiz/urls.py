from django.urls import path
from .views import *

urlpatterns = [
    path('quiz_index/', quiz_index, name="quiz_index"),
]