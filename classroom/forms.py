from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from classroom.models import Student






class ProfileUpdateForm(forms.ModelForm):

    class Meta:

          model = Student
          fields = ['prenom','nom', 'adresse_email','numero_telephone','niveau_etude','etudiant', 'annee', 'formation_1', 'formation_2', 'motivation']

