from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Text(models.Model):

    value = models.TextField()
    hash  = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="texts", null=True)

