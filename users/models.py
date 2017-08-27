from django.db import models
from steps.models import Step

GENDER_CHOICES = (
    ('f', 'Female'),
    ('m', 'Male'),
    ('o', 'Undisclosed'),
)

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " " + self.surname

    def full_name(self):
        return self.name + " " + self.surname


class UserStep(models.Model):
    user_id = models.ForeignKey(User)
    step_id = models.ForeignKey(Step)