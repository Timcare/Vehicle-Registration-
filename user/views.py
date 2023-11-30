from django.shortcuts import render,redirect
from django import views
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import login

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

