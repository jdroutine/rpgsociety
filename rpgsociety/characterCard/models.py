from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name


