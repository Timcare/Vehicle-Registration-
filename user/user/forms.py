from django import forms
from . models import Profiles,Bio
from django.contrib.auth.models import User

class BioForm(forms.ModelForm):

    class Meta:
        model=Bio
        fields=("middlename","date_of_birth","state","local_government","blood_group","upload_driving_school_certificate","class_of_vehicle",
        "issue_date","expiry_date")

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profiles
        fields=("photo",)

class UserForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields=("first_name","last_name",)

