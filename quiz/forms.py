from django import forms
from .models import *


class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        exclude = ['created_by', 'active']
        labels = {
            'name': 'Quiz Name',
            'amount_of_questions': 'Number of questions'
        }

