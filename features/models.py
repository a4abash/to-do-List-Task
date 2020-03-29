from django.db import models


# Create your models here.
class required(models.Model):
    title = models.CharField(max_length=200)
    date_to_complete = models.DateField()

    def __str__(self):
        return self.title