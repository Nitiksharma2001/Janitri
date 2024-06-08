from django.db import models
from django.contrib.auth.models import User

class Operation(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    heart_rate = models.PositiveIntegerField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    role = models.CharField(max_length=100)