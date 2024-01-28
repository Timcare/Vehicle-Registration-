from django import forms
from . models import Vehicle,VehicleInfo,OwnerInfo,Individual,Company

class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=("__all__")

class VehicleInfoForm(forms.ModelForm):
    class Meta:
        model=VehicleInfo
        fields=("__all__")

class OwnerInfoForm(forms.ModelForm):
    class Meta:
        model=OwnerInfo
        fields=("__all__")

class IndividualForm(forms.ModelForm):
    class Meta:
        model=Individual
        fields=("__all__")

class CompanyForm(forms.ModelForm):
    
    class Meta:
        model=Company
        fields=("__all__")


