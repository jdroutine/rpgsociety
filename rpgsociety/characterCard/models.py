from django.db import models

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

    def __str__(self):
        return self.name


class Home(models.Model):
    title = models.CharField(max_length=255)
    titleSpan = models.CharField(max_length=255, null=True)
    body = models.TextField(max_length=255)

    def __str__(self):
        return self.title
