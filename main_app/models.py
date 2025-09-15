from django.db import models

# Create your models here.

HOUSES = (
    ('G', 'Gryffindor'),
    ('S', 'Slytherin'),
    ('R', 'Ravenclaw'),
    ('H', 'Hufflepuff'),
)

class Wizard(models.Model):
    name = models.CharField(max_length=100)
    house = models.CharField(max_length=1, choices=HOUSES, default=HOUSES[0][0])
    age = models.IntegerField()

    def __str__(self):
        return self.name