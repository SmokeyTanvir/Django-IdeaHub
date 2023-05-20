from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Opinion(models.Model):
    opinion = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True)
    is_authorized = models.BooleanField(default=False)

    def __str__(self):
        return self.opinion