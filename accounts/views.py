from django.shortcuts import render
from .models import users,patient,doctor
from .forms import user_sign,doctor_sign,patient_sign

def patient_form(request):
    d_form = patient_sign()
    form = user_sign()
    return render(request,"accounts/register.html",{"d_form":d_form,"form":form})


def doctor_form(request):
    d_form = doctor_sign()
    form = user_sign()
    return render(request,"accounts/register.html",{"d_form":d_form,"form":form})


def user_login(request):
    return render(request,"accounts/login.html",{})




def profile(request,slug):
    return render(request,"accounts/profile.html",{})
