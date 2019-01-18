from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    age = models.IntegerField()

    def __str__(self):
        return self.name
