from django.db import models
from django.conf import settings


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interviewing', 'Interviewing'),
        ('Offer Received', 'Offer Received'),
        ('Rejected', 'Rejected'),
        ('Withdrawn', 'Withdrawn'),
]


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_applications')
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    application_date = models.DateField()
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='Applied')
    notes = models.TextField(blank=True)
    link_to_posting = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-application_date', '-updated_at']


    def __str__(self):
        return f"{self.company_name} - {self.job_title} ({self.status})"
