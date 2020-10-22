from django import forms
from .models import *


class NewQuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        exclude = ['created_by', 'active']
        labels = {
            'name': 'Quiz Name',
            'amount_of_questions': 'Number of questions'
        }


class EditQuizQuestionLimit(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ['amount_of_questions']
        labels = {
            'amount_of_questions': 'Number of questions'
        }