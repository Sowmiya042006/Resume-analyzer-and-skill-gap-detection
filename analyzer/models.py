from django.db import models
from django.contrib.auth.models import User

class JobRole(models.Model):
    title = models.CharField(max_length=100)
    # Storing skills as a JSON list, e.g., ["Python", "Django", "SQL"]
    required_skills = models.JSONField(default=list) 

    def __str__(self):
        return self.title

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE, null=True, blank=True)
    # Parsed text content
    parsed_content = models.TextField(blank=True, null=True)
    # Skills found in the resume
    extracted_skills = models.JSONField(default=list, blank=True)
    # Missing skills based on the job role
    missing_skills = models.JSONField(default=list, blank=True)
    # Resume match score (0-100)
    match_score = models.IntegerField(default=0)

    def __str__(self):
        return f"Resume {self.id} - {self.uploaded_at.strftime('%Y-%m-%d')}"
