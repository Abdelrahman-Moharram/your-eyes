from django.shortcuts import render

def register(request):
    return render(request,"accounts/register.html",{})




def user_login(request):
    return render(request,"accounts/login.html",{})




def profile(request,slug):
    return render(request,"accounts/profile.html",{})
