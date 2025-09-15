from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Wizard:
    def __init__(self, name, house, age):
        self.name = name
        self.house = house
        self.age = age

# Create a list of Cat instances
wizards = [
    Wizard('Harry', 'gryffindor', 17),
    Wizard('Hermione', 'gryffindor', 17),
    Wizard('Ron', 'gryffindor', 17),
]

def wizard_index(request):
    return render(request, 'wizards/index.html', {'wizards': wizards})