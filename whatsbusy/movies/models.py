from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    imdb_rating = models.FloatField(max_length=2)

    def __str__(self):
        return self.name
