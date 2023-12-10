from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . forms import VehicleForm,VehicleInfoForm,OwnerInfoForm,IndividualForm,CompanyForm,OtherInfoForm
from . models import OwnerInfo
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

@login_required
def dashboard(request):
    if request.method=='POST':
        vehicleform=VehicleForm(request.POST)
        vehicleinfo=VehicleInfoForm(request.POST)
        ownerinfo=OwnerInfoForm(request.POST)
        individualform=IndividualForm(request.POST)
        companyform=CompanyForm(request.POST,auto_id='fields_for_%s',)
        otherform=OtherInfoForm(request.POST)
        print(companyform)
        if vehicleform.is_valid() and vehicleinfo.is_valid() and ownerinfo.is_valid() and individualform.is_valid() and companyform.is_valid() and otherform.is_valid() :
            vehicleform.save()
            vehicleinfo.save()
            ownerinfo.save()
            individualform.save()
            companyform.save()
            otherform.save()
            messages.success(request,'Form submitted successfully')
            return redirect("dashboard")

        else:
            messages.error(request,'Error occured while saving')
            return redirect("dashboard")
    else:
        vehicleform=VehicleForm()
        vehicleinfo=VehicleInfoForm()
        ownerinfo=OwnerInfoForm()
        individualform=IndividualForm()
        companyform=CompanyForm(auto_id='fields_for_%s')
        otherform=OtherInfoForm()

    return render(request,'dashboard.html',{'vehicleform':vehicleform,'vehicleinfo':vehicleinfo,'ownerinfo':ownerinfo,
    'individualform':individualform,'companyform':companyform,'otherform':otherform})
