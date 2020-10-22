from django import forms
from .models import *


class NewQuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        exclude = ['created_by', 'active']

