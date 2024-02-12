from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Vehicle,VehicleInfo
from . forms import VehicleForm,VehicleInfoForm,OwnerInfoForm,IndividualForm,CompanyForm
from . models import OwnerInfo
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import get_template
from  PyPDF2 import PdfFileWriter,PdfFileReader
from django.contrib import messages
from user.models import Profiles
import requests
import pdfkit
config=pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

@login_required
def dashboard(request):
    users=Profiles.objects.get(user=request.user)
    if request.method=='POST':
        vehicleform=VehicleForm(request.POST,instance=users)
        vehicleinfo=VehicleInfoForm(request.POST)
        ownerinfo=OwnerInfoForm(request.POST)
        individualform=IndividualForm(request.POST)
        companyform=CompanyForm(request.POST,auto_id='fields_for_%s',)
        
        if vehicleform.is_valid() and ownerinfo.is_valid() and individualform.is_valid() and companyform.is_valid() :
            vehicleform.save()
            #vehicleinfo.save()
            ownerinfo.save()
            individualform.save()
            companyform.save()
            
            messages.success(request,'Form submitted successfully,Your request is pending')
            return redirect("home:dashboard")

        else:
            messages.error(request,'Error occured while saving')
            return redirect("home:dashboard")
    else:
        vehicleform=VehicleForm(instance=users)
        vehicleinfo=VehicleInfoForm()
        ownerinfo=OwnerInfoForm()
        individualform=IndividualForm()
        companyform=CompanyForm(auto_id='fields_for_%s')

    if request.user.profiles.approved==True:
        return render(request, 'confirm_reg.html', {})
       

    return render(request,'vehicleregistration.html',{'vehicleform':vehicleform,'vehicleinfo':vehicleinfo,'ownerinfo':ownerinfo,
    'individualform':individualform,'companyform':companyform})

@login_required
def confirm_reg(request):
    return render(request,'confirm_reg.html')
@login_required
def checkout(request):
    vehicle=Vehicle.objects.get(user=request.user)
    vehicleinfo=VehicleInfo.objects.get(vehicle=vehicle)
    return render(request,'checkout.html',{'vehicles':vehicle,'vehicleinfo':vehicleinfo})
    
@login_required
def generatePDF(request):
    pdf=pdfkit.from_url(request.build_absolute_uri(reverse('home:home')),False,configuration=config)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposiion']='attachment; filename="file_name.pdf"'
    return response

def append_pdf(pdf,output):
    [output.addPage(pdf.getPage(page_num)) for page_num in range(pdf.numPages)]

def render_to_pdf():
    t=get_template("home/checkout.html")
    vehicle=Vehicle.objects.get(user=request.user)
    vehicleinfo=VehicleInfo.objects.get(vehicle=vehicle)
    c={'vehicles':vehicle,'vehicleinfo':vehicleinfo}

    html=t.render(c)
    pdfkit.from_string(html,r'C:\Users\idowu\Desktop\Django\Final\Final\static.pdf')
    output=PdfFileWriter()
    append_pdf(PdfFileReader(open(r'C:\Users\idowu\Desktop\Django\Final\Final\static.pdf','rb')),output)
    attaches=Attachment.objects.all()

    for attach in attaches:
        append_pdf(PdfFileReader(open('attach.file.path','rb')),output)
    output.write(open(r"C:\Users\idowu\Desktop\Django\Final\Final\static.pdf",'wb'))
