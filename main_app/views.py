from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests
from .models import Wizard, Wand, Spell
from .forms import WandForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def wizard_index(request):
    collected = Wizard.objects.filter(is_collected=True, user=request.user).order_by('name')
    return render(request, 'wizards/index.html', {'wizards': collected})

@login_required
def wizard_detail(request, wizard_id):
    wizard = Wizard.objects.get(id=wizard_id)

    if Spell.objects.count() == 0:
        url = 'https://hp-api.onrender.com/api/spells'
        response = requests.get(url)
        if response.status_code == 200:
            for i in response.json():
                if not Spell.objects.filter(name=i.get('name')).exists():
                    Spell.objects.create(
                        name=i.get('name', 'Unknown'),
                        description=i.get('description', 'No description available')
                    )

    if request.method == 'POST':
        spell_id = request.POST.get('spell')
        if spell_id:
            spell = Spell.objects.get(id=spell_id)
            wizard.spells.add(spell)
            return redirect('wizard-detail', wizard_id=wizard_id)

    wand_form = WandForm()
    all_spells = Spell.objects.all().order_by('name')

    return render(request, 'wizards/detail.html', {
        'wizard': wizard,
        'wand_form': wand_form,
        'all_spells': all_spells,
    })

@login_required
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
                        patronus=i.get('patronus', 'Unknown'),
                        user = (request.user)
                    )

    uncollected_wizards = Wizard.objects.filter(is_collected=False).order_by('name')

    if request.method == 'POST':
        wizard_id = request.POST.get('wizard')
        if wizard_id and request.user.is_authenticated:
            wizard = Wizard.objects.get(id=wizard_id)
            wizard.is_collected = True
            wizard.user = request.user
            wizard.save()
            return redirect('wizard-detail', wizard_id=wizard_id)

    return render(request, 'main_app/wizard_form.html', {'all_wizards': uncollected_wizards})


@login_required
def add_wand(request, wizard_id):
    form = WandForm(request.POST)

    if form.is_valid():
        new_wand = form.save(commit=False)
        new_wand.wizard_id = wizard_id
        new_wand.save()
    return redirect('wizard-detail', wizard_id=wizard_id)


class WandUpdate(LoginRequiredMixin, UpdateView):
    model = Wand
    fields = ['core', 'wood', 'length']


class WandDelete(LoginRequiredMixin, DeleteView):
    model = Wand
    success_url = '/wizards/'

@login_required
def spell_index(request):
    if Spell.objects.count() == 0:
        url = 'https://hp-api.onrender.com/api/spells'
        response = requests.get(url)
        if response.status_code == 200:
            for i in response.json():
                if not Spell.objects.filter(name=i.get('name')).exists():
                    Spell.objects.create(
                        name=i.get('name', 'Unknown'),
                        description=i.get('description')
                    )

    
    query = request.GET.get('q', '')  
    if query:
        all_spells = Spell.objects.filter(name__icontains=query)
    else:
        all_spells = Spell.objects.filter(is_collected=False).order_by('name')

   
    if request.method == 'POST':
        spell_id = request.POST.get('spell')
        if spell_id:
            spell = Spell.objects.get(id=spell_id)
            spell.is_collected = True
            spell.save()
            all_spells = Spell.objects.filter(is_collected=False).order_by('name')

    return render(request, 'spells/index.html', {'all_spells': all_spells, 'query': query})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
           
            login(request, user)
            return redirect('wizard-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
  