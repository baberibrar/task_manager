from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

class Task(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )
    PRIORITY_CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    due_date = models.DateTimeField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Medium')
    category = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})


class ActivityLog(models.Model):
    ACTION_CHOICES = (
        ('Create', 'Create'),
        ('Update', 'Update'),
        ('Delete', 'Delete'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=6, choices=ACTION_CHOICES)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
