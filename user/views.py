from django.shortcuts import render,redirect
from django import views
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import login
from . forms import ProfileForm,UserForm

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
            return redirect("home")
        else:
            messages.error(request,'An error occur processing your request')
            return render(request,'registration/register.html',{'register_form':register_form})

def Profile(request):
    if request.method=="POST":
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.FILES)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            messages.success(request,'Profile updated successfully')
            return redirect("profile")
        else:
            messages.error(request,'Error occour updating your profile')
            return redirect("profile")
    else:
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.FILES)
    return render(request,'profile.html',{'profileform':profileform,'userform':userform})


