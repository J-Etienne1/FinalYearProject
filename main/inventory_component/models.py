from django.db import models

class Inventory(models.Model):
    item = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()