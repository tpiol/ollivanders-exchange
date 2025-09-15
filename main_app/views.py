from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests

from .models import Wizard


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def wizard_index(request):
    collected = Wizard.objects.filter(is_collected=True).order_by('name')
    return render(request, 'wizards/index.html', {'wizards': collected})

def wizard_detail(request, wizard_id):
    wizard = Wizard.objects.get(id=wizard_id)
    return render(request, 'wizards/detail.html', {'wizard': wizard})

def choose_wizard(request):

    if Wizard.objects.count() == 0:
        url = 'https://hp-api.onrender.com/api/characters'
        response = requests.get(url)
        if response.status_code == 200:
            for i in response.json():
                if not Wizard.objects.filter(name=i.get('name')).exists():
                    Wizard.objects.create(
                        name=i.get('name', 'Unknown'),
                        image=i.get('image', ''),
                        house=i.get('house', '')[:1].upper() if i.get('house') else 'G',
                        dateOfBirth=i.get('dateOfBirth') or 'Unknown',
                        patronus=i.get('patronus', 'Unknown')
                    )

    uncollected_wizards = Wizard.objects.filter(is_collected=False).order_by('name')

    if request.method == 'POST':
        wizard_id = request.POST.get('wizard')
        if wizard_id:
            wizard = Wizard.objects.get(id=wizard_id)
            wizard.is_collected = True
            wizard.save()
            return render(request, 'wizards/detail.html', {'wizard': wizard})

    return render(request, 'main_app/wizard_form.html', {'all_wizards': uncollected_wizards})
    

class WizardDelete(DeleteView):
    model = Wizard
    success_url = '/wizards/'