from django.db import models
from django.contrib.auth.models import User

class Inventory(models.Model):
    item = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')