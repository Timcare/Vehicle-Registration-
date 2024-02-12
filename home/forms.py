from django import forms
from . models import Vehicle,VehicleInfo,OwnerInfo,Individual,Company

class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=("vehicle_category","vehicle_sub_category","old_plate_number","vehicle_maker","color","fuel_type","year_of_manufacturer","plate_number")

class VehicleInfoForm(forms.ModelForm):
    class Meta:
        model=VehicleInfo
        fields=("model","engine_number","policy_number","vehicle_type","chassis_no","engine_capacity","tank_capacity","odometer","vehicle")

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


