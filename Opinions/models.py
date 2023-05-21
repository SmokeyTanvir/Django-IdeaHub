from django.db import models
from django.contrib.auth.models import User 

class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    opinion = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.opinion
