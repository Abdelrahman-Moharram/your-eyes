from django.shortcuts import render,redirect
from django.contrib import messages
from .models import users,patient,doctor
from .forms import user_sign,doctor_sign,patient_sign,f_dieseas,dieseas

def patient_form(request):
    d_form = patient_sign()
    form   = user_sign()
    d,f_d  = f_dieseas(),dieseas()

    if request.method == "POST":
        form = user_sign(request.POST , request.FILES)
        d_form = patient_sign(request.POST,request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.user_type = "Patient"
            form.save()
            if d_form.is_valid():
                d_form = d_form.save(commit = False)
                d_form.user = form
                d_form.save()
                



                messages.info(request,form.slug+"added succesfully please login")
                return redirect("accounts:login")
    return render(request,"accounts/register.html",{"d_form":d_form,"form":form,"diesease":d,"fd":f_d})


def doctor_form(request):
    d_form = doctor_sign()
    form = user_sign()

    if request.method == "POST":
        form = user_sign(request.POST , request.FILES)
        d_form = doctor_sign(request.POST,request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.user_type = "Doctor"
            form.save()
            if d_form.is_valid():
                d_form = d_form.save(commit = False)
                d_form.user = form
                d_form.save()
                messages.info(request,form.slug+"added succesfully please login")
                return redirect("accounts:login")

    return render(request,"accounts/register.html",{"d_form":d_form,"form":form})


def user_login(request):
    return render(request,"accounts/login.html",{})




def profile(request,slug):
    return render(request,"accounts/profile.html",{})
