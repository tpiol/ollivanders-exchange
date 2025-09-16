from django.db import models
from django.urls import reverse

# Create your models here.

HOUSES = (
    ('G', 'Gryffindor'),
    ('S', 'Slytherin'),
    ('R', 'Ravenclaw'),
    ('H', 'Hufflepuff'),
)

WOODS = (
    ("AC", "Acacia"),
    ("AL", "Alder"),
    ("AP", "Apple"),
    ("AS", "Ash"),
    ("AN", "Aspen"),
    ("BE", "Beech"),
    ("BT", "Blackthorn"),
    ("BW", "Black Walnut"),
    ("CE", "Cedar"),
    ("CH", "Cherry"),
    ("CS", "Chestnut"),
    ("CY", "Cypress"),
    ("DO", "Dogwood"),
    ("EB", "Ebony"),
    ("EL", "Elm"),
    ("FI", "Fir"),
    ("HA", "Hawthorn"),
    ("HZ", "Hazel"),
    ("HO", "Holly"),
    ("HM", "Hornbeam"),
    ("LA", "Larch"),
    ("LR", "Laurel"),
    ("MA", "Maple"),
    ("OA", "Oak"),
    ("PE", "Pear"),
    ("PI", "Pine"),
    ("PO", "Poplar"),
    ("RD", "Redwood"),
    ("RW", "Rowan"),
    ("SL", "Silver Lime"),
    ("SP", "Spruce"),
    ("SY", "Sycamore"),
    ("VI", "Vine"),
    ("WA", "Walnut"),
    ("WI", "Willow"),
    ("YE", "Yew"),
)

CORES = (
    ("PF", "Phoenix Feather"),
    ("DH", "Dragon Heartstring"),
    ("UH", "Unicorn Hair"),
    ("TT", "Thestral Tail Hair"),
    ("VH", "Veela Hair"),
    ("TW", "Troll Whisker"),
    ("KH", "Kelpie Hair"),
    ("TF", "Thunderbird Tail Feather"),
    ("WC", "Wampus Cat Hair"),
    ("WR", "White River Monster Spine"),
    ("RH", "Rougarou Hair"),
    ("HS", "Horned Serpent Horn"),
    ("JA", "Jackalope Antler"),
    ("BH", "Basilisk Horn"),
    ("SH", "Snallygaster Heartstring"),
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
    

class Wand(models.Model):
    wood = models.CharField(max_length=2, choices=WOODS, default=WOODS[0][0])
    core = models.CharField(max_length=2, choices=CORES, default=CORES[0][0])
    length = models.FloatField()

    wizard = models.ForeignKey(Wizard, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.length}\" {self.get_wood_display()} with {self.get_core_display()}"
    
    def get_absolute_url(self):
        return reverse('wizard-detail', kwargs={'wizard_id': self.wizard.id})