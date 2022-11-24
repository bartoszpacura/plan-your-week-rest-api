from django.db import models

# Create your models here.


class Day(models.Model):
    day = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)

    def __str__(self):
        return self.day
