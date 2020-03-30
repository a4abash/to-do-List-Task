from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TaskFeatures(models.Model):
    title = models.CharField(max_length=200)
    date_to_complete = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title