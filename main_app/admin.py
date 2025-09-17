from django.contrib import admin
from .models import Wizard, Wand, Spell

# Register your models here.

admin.site.register(Wizard)
admin.site.register(Wand)
admin.site.register(Spell)