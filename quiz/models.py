from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from accounts.models import Profile
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Profile, related_name='quizzes', on_delete=models.CASCADE)
    last_updated = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)
    amount_of_questions = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)], default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")


class Question(models.Model):
    quest = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    order = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)], default=1)

    def __str__(self):
        return self.quest