from django.shortcuts import render
from .models import Wizard


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def wizard_index(request):
    wizards = Wizard.objects.all()
    return render(request, 'wizards/index.html', {'wizards': wizards})

def wizard_detail(request, wizard_id):
    wizard = Wizard.objects.get(id=wizard_id)
    return render(request, 'wizards/detail.html', {'wizard': wizard})