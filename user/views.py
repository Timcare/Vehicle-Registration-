from django.shortcuts import render,redirect,get_object_or_404
from django import views
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from . forms import ProfileForm,BioForm,UserForm
from .models import Bio,Profiles

# Create your views here.
def base(request):
    return render(request,'base.html')

class RegisterForm(View):
    def get(self,request):
            register_form=UserCreationForm()
            return render(request,'registration/register.html',{'register_form':register_form})
    def post(self,request):
        register_form=UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user=register_form.save()
            login(request,user)
            return redirect("home:home")
        else:
            messages.error(request,'An error occur processing your request')
            return render(request,'registration/register.html',{'register_form':register_form})

@login_required
def Profile(request):
    
    if request.method=="POST":
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES,instance=request.user.profiles)
        bioform=BioForm(request.POST,request.FILES)
        
        if userform.is_valid() and profileform.is_valid() and bioform.is_valid():
            userform.save()
            profileform.save()
            profile=bioform.save(commit=False)
            profile.profiles=request.user.profiles
            profile.save()

            messages.success(request,'Profile updated successfully')
            return redirect("profile")
        else:
            messages.error(request,'Error occur updating your profile')
            return redirect("profile")
    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=request.user.profiles)
        bioform=BioForm()
    return render(request,'profile.html',{'userform':userform,'profileform':profileform,'bioform':bioform})

@login_required
def License(request):
    profiles=Bio.objects.filter(profiles=request.user.profiles)
    return render(request,'drivers_license.html',{'profiles':profiles})