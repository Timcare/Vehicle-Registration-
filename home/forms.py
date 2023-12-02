from django import forms
from . models import Vehicle,VehicleInfo

class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=("__all__")

class VehicleInfoForm(forms.ModelForm):
    class Meta:
        model=VehicleInfo
        fields=("__all__")
