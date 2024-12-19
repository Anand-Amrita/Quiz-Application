from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = (('admin', 'Admin'), ('student', 'Student'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    student_id = models.CharField(max_length=50, blank=True, null=True, unique=True)  # Student ID
    age = models.PositiveIntegerField(blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)  # Add this field
    def __str__(self):
        return self.username

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_question_counts(self):
        #Returns a tuple of (easy, medium, hard) question counts.
        easy_count = Question.objects.filter(subject=self, difficulty='easy').count()
        medium_count = Question.objects.filter(subject=self, difficulty='medium').count()
        hard_count = Question.objects.filter(subject=self, difficulty='hard').count()
        return easy_count, medium_count, hard_count

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(max_length=50)  # Add this line
    difficulty = models.CharField(max_length=50)
    options = models.JSONField(null=True, blank=True)  # For MCQs only
    correct_answer = models.TextField()  # Add this line

    def __str__(self):
        return self.question_text


class UserAnswer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_selected = models.CharField(max_length=255, default="No Answer")
    correct = models.BooleanField(default=False)
    difficulty = models.CharField(max_length=50, default="Medium")
    time_taken = models.FloatField(default=0.0)

class Result(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    quiz_type = models.CharField(max_length=50)
    correct_answers = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    marks = models.FloatField(default=0.0)
    grade = models.CharField(max_length=2, default="F")
    times = models.JSONField(default=list)  # Storing times per question in a list.
