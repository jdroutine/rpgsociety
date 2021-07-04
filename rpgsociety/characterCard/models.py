from django.db import models

# Create your models here.


class Character(models.Model):
    # status choices
    statusChoices = (
        ('Normalny', 'Normal'),
        ('Zdenerwowanie', 'Nervousness'),
        ('Przerażenie', 'Horror'),
        ('Zmęczenie', 'Fatigue'),
        ('Zranienie', 'Injury'),
        ('Wycieńczenie', 'Weakness')
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    status = models.CharField(max_length=50, choices=statusChoices, null=True)
    luck = models.IntegerField(null=True)
    item = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
