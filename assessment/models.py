from django.db import models
from analyzer.models import JobRole

class Question(models.Model):
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)
    # Store options as a list of strings
    options = models.JSONField(default=list)
    # Index of the correct option (0-3) or the string value
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.job_role.title} - {self.text[:50]}"

class TestSession(models.Model):
    resume = models.ForeignKey('analyzer.Resume', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)
