from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . forms import VehicleForm,VehicleInfoForm

# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

@login_required
def dashboard(request):
    vehicleform=VehicleForm
    vehicleinfo=VehicleInfoForm
    return render(request,'dashboard.html',{'vehicleform':vehicleform,'vehicleinfo':vehicleinfo})