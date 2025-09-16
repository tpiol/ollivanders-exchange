from django import forms
from .models import Wand

class WandForm(forms.ModelForm):
    class Meta:
        model = Wand
        fields = ['wood', 'core', 'length']
