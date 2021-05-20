from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django.utils.html import escape, mark_safe
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.dispatch import receiver
import re
from django.utils import timezone
from djrichtextfield.widgets import RichTextWidget
from djrichtextfield.models import RichTextField


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)



class Student(models.Model):
    nom = models.CharField(max_length=270,verbose_name= u"Nom de famille  ")
    prenom = models.CharField(max_length=270,verbose_name= u"Prénom   ")
    adresse_email = models.EmailField(max_length=100,verbose_name=u"email ",)
    numero_telephone=models.IntegerField(verbose_name= u"Numéro de téléphone ",  null=True, blank=True)
    niveau_etude=models.CharField(max_length=100,verbose_name= u"Niveau d'étude ",  null=True, blank=True)
    etudiant =models.BooleanField(verbose_name= u"Ancien étudiant de l'ENSGSI ",  default=False)
    annee=models.CharField(max_length=100, verbose_name= u"Si oui année de l'obtention du diplôme ",   null=True, blank=True)
    formation_1=models.BooleanField(verbose_name= u"Je souhaite également m'inscrire le 29 Juin à la formation payante ",  default=False)    
    formation_2=models.BooleanField(verbose_name= u"Je souhaite également m'inscrire le 30 Juin à la formation payante ",  default=False) 
    motivation = RichTextField(blank=True, null=True)



    def __str__(self):
        if self.name==None:
           return "ERROR-STUDENT NAME IS NULL"
        return self.name

