from django.db import models
from django.db.models.base import Model

# Create your models here.


class Character(models.Model):
    # status choices
    statusChoices = (
        ('Brak', 'None'),
        ('Zdenerwowanie', 'Nervousness'),
        ('Przerażenie', 'Horror'),
        ('Zmęczenie', 'Fatigue'),
        ('Zranienie', 'Injury'),
        ('Wycieńczenie', 'Weakness')
    )
    # skill point choices
    skillChoices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    expChoices = (
        ('1/10', '1'),
        ('2/10', '2'),
        ('3/10', '3'),
        ('4/10', '4'),
        ('5/10', '5'),
        ('6/10', '6'),
        ('7/10', '7'),
        ('8/10', '8'),
        ('9/10', '9'),
        ('10/10', '10')
    )

    name = models.CharField(max_length=255)
    avatar = models.ImageField(blank=True, upload_to='images')
    type = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    motivation = models.CharField(max_length=50, null=True)
    support = models.CharField(max_length=50, null=True)
    problem = models.CharField(max_length=255, null=True)
    pride = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, null=True)
    song = models.CharField(max_length=255, null=True)
    status1 = models.CharField(max_length=50, choices=statusChoices, null=True)
    status2 = models.CharField(max_length=50, choices=statusChoices, null=True)
    status3 = models.CharField(max_length=50, choices=statusChoices, null=True)
    status4 = models.CharField(max_length=50, choices=statusChoices, null=True)
    status5 = models.CharField(max_length=50, choices=statusChoices, null=True)
    luck = models.IntegerField(choices=skillChoices, null=True)
    item = models.CharField(max_length=50, null=True)
    exp = models.CharField(max_length=50,choices=expChoices, null=True)

    body = models.IntegerField(choices=skillChoices, null=True)
    technique = models.IntegerField(choices=skillChoices, null=True)
    heart = models.IntegerField(choices=skillChoices, null=True)
    mind = models.IntegerField(choices=skillChoices, null=True)

    sneaking = models.IntegerField(choices=skillChoices, null=True)
    strength = models.IntegerField(choices=skillChoices, null=True)
    movement = models.IntegerField(choices=skillChoices, null=True)
    diy = models.IntegerField(choices=skillChoices, null=True)
    coding = models.IntegerField(choices=skillChoices, null=True)
    analisys = models.IntegerField(choices=skillChoices, null=True)
    conversance = models.IntegerField(choices=skillChoices, null=True)
    charm = models.IntegerField(choices=skillChoices, null=True)
    conduction = models.IntegerField(choices=skillChoices, null=True)
    investigation = models.IntegerField(choices=skillChoices, null=True)
    understanding = models.IntegerField(choices=skillChoices, null=True)
    empathy = models.IntegerField(choices=skillChoices, null=True)
    headquarters = models.TextField(max_length=255, null=True)

    realtion1 = models.CharField(max_length=255, null=True)
    realtion2 = models.CharField(max_length=255, null=True)
    realtion3 = models.CharField(max_length=255, null=True)
    realtion4 = models.CharField(max_length=255, null=True)
    realtionBn1 = models.CharField(max_length=255, null=True)
    realtionBn2 = models.CharField(max_length=255, null=True)
    realtionBn3 = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Home(models.Model):
    title = models.CharField(max_length=255)
    titleSpan = models.CharField(max_length=255, null=True)
    body = models.TextField(max_length=255)

    def __str__(self):
        return self.title

class Map(models.Model):
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(blank=True, upload_to='images')
    