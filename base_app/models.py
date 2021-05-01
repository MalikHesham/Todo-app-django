from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True , blank = True)
    title = models.CharField(max_length=100, null = True , blank = True)
    desc = models.TextField( null = True , blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    task_completed = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['task_completed']