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
    image = models.URLField()
    house = models.CharField(max_length=1, choices=HOUSES, default=HOUSES[0][0])
    dateOfBirth = models.CharField(max_length=50, blank=True, null=True)
    patronus = models.CharField(max_length=50)
    is_collected = models.BooleanField(default=False)

    def __str__(self):
        return self.name