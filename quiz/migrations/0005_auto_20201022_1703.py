# Generated by Django 3.1.2 on 2020-10-22 16:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_quiz_amount_of_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='amount_of_questions',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)]),
        ),
    ]