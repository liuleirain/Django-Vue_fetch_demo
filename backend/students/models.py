from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=140)
    course = models.CharField(max_length=140)
    rating = models.IntegerField()

    class Meta:
        ordering = ['name']
