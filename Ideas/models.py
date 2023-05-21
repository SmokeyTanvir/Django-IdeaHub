from django.db import models
from django.contrib.auth.models import User 

class Idea(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    idea = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.idea} ~ {self.author}"
