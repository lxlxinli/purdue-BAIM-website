from django.db import models
from django_matplotlib import MatplotlibFigureField

# Create your models here.

class posters(models.Model):
    Venue = models.CharField(max_length = 100,unique=True)
    YEAR2017 = models.IntegerField(default=0)
    YEAR2018 = models.IntegerField(default=0)
    YEAR2019 = models.IntegerField(default=0)
    YEAR2020 = models.IntegerField(default=0)

    def __str__(self):
        return self.Venue

class papers(models.Model):
    Venue = models.CharField(max_length = 100,unique=True)
    YEAR2017 = models.IntegerField(default=0)
    YEAR2018 = models.IntegerField(default=0)
    YEAR2019 = models.IntegerField(default=0)
    YEAR2020 = models.IntegerField(default=0)

    def __str__(self):
        return self.Venue