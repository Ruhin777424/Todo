from django.db import models
from django.conf import settings


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    
    # Priority: 1 - Low, 2 - Medium, 3 - High
    PRIORITY_LOW = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_HIGH = 3
    PRIORITY_CHOICES = (
        (PRIORITY_LOW, 'Low'),
        (PRIORITY_MEDIUM, 'Medium'),
        (PRIORITY_HIGH, 'High'),
    )
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM)
    
    # Status: active, completed (in archive), deleted (in trash archive)
    STATUS_ACTIVE = 'active'
    STATUS_COMPLETED = 'completed'
    STATUS_DELETED = 'deleted'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_DELETED, 'Deleted'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    reminder_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
