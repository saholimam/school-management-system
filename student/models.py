from django.db import models

class Student(models.Model):
    GENDER_CHOICE = (
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    )
    name = models.CharField(max_length=120)
    father = models.CharField(max_length=120)
    mother = models.CharField(max_length=120)
    photo = models.ImageField(upload_to= 'uploads/')
    roll = models.IntegerField(unique=True)
    reg = models.IntegerField(unique=True)
    sex = models.CharField(choices=GENDER_CHOICE,max_length=6)
    dob = models.DateField()
    time = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.roll
