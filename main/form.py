from django.forms import widgets
from main import models
from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import ForUser,University,NotesUniversity,Jeunes,NotesJeunes
class UserLogin(forms.ModelForm):
    class Meta:
        model=ForUser
        fields=["username","password"]
        widgets={"username":forms.TextInput(attrs={"class":"form-control","id":"username","placeholder":"Username"}),
        "password":forms.PasswordInput(attrs={"class":"form-control","id":"password","placeholder":"Password"}),
        }

class UserSingin(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"] 
        widgets={"username":forms.TextInput(attrs={"class":"form-control","id":"username","placeholder":"Username"}),
        "email":forms.EmailInput(attrs={"class":"form-control","id":"email","placeholder":"Email"}),
        "password1":forms.PasswordInput(attrs={"class":"form-control","id":"password1"}),
        }

class UniversityRegistration(forms.ModelForm):
    class Meta:
        model=University
        fields=["name","email","date_naissance","telephone","ville","name_pere","name_mere","imageprofile","designation","institution",
        "fillier","batch","address","telephone_mere","telephone_pere"]
        widgets={
            "date_naissance":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "batch":forms.Select(attrs={'class':'form-control'}),
            "designation":forms.Select(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={"class":"form-control","id":"email"}),
        }

class NotesUniversityForm(forms.ModelForm):
    class Meta:
        model=NotesUniversity
        fields=['university','year','sem','matiere','notes','characteristic','moyen']
        widgets={'university':forms.Select(attrs={'class':'form-control'}),
        'sem':forms.Select(attrs={'class':'form-control'}),
        'year':forms.Select(attrs={'class':'form-control'}),
        'characteristic':forms.Select(attrs={'class':'form-control'}),

        }

class JeunesRegistration(forms.ModelForm):
    class Meta:
        model=Jeunes
        fields=["name","date_naissance","ville","name_pere","name_mere","imageprofile","designation","institution",
        "batch","address","telephone_mere","telephone_pere"]
        widgets={
            "date_naissance":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "batch":forms.Select(attrs={'class':'form-control'}),
            "designation":forms.Select(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={"class":"form-control","id":"email"}),
        }

class NotesJeunesForm(forms.ModelForm):
    class Meta:
        model=NotesJeunes
        fields=['jeunes','year','sem','matiere','notes','characteristic','moyen']
        widgets={'jeunes':forms.Select(attrs={'class':'form-control'}),
        'sem':forms.Select(attrs={'class':'form-control'}),
        'year':forms.Select(attrs={'class':'form-control'}),
        'characteristic':forms.Select(attrs={'class':'form-control'}),

        } 


