from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login

from django.shortcuts import render, redirect
from .forms import RegistrationForm

def user_register(request):
    if(request.method == "POST"):  
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "users/register.html",{"form":form})

def user_login(request):

    if(request.method == "POST"):
        usr = request.POST["username"]
        pwd = request.POST["password"]

        user = authenticate(request, username=usr, password=pwd)

        if(user is not None):
            #login succeeded
            login(request, user)
            return redirect("home")

    return render(request, "users/login.html")
