from django.db import models

class ToDo(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline=models.DateTimeField(null=True)
    def __str__(self):
        return self.task