# Generated by Django 3.1.2 on 2020-10-21 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_remove_profile_current_save'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('archived', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='accounts.profile')),
            ],
        ),
    ]
