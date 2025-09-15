from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wizards/', views.wizard_index, name='wizard-index'),
    path('wizards/<int:wizard_id>/', views.wizard_detail, name='wizard-detail'),
    path('wizards/choose/', views.choose_wizard, name='choose-wizard'),
    path('wizards/<int:pk>/delete/', views.WizardDelete.as_view(), name='wizard-delete'),
]