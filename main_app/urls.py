from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wizards/', views.wizard_index, name='wizard-index'),
    path('wizards/<int:wizard_id>/', views.wizard_detail, name='wizard-detail'),
    path('wizards/choose/', views.choose_wizard, name='choose-wizard'),
    path('wands/<int:pk>/delete/', views.WandDelete.as_view(), name='wand-delete'),
    path('wands/<int:pk>/update/', views.WandUpdate.as_view(), name='wand-update'),
    path('wizards/<int:wizard_id>/add-wand/', views.add_wand, name='add-wand'),
    path('spells/', views.spell_index, name='spell-index'),
]