from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .forms import user_registration_form

def user_register(request):
    if(request.method == "POST"):
        form = user_registration_form(request.POST)

        if form.is_valid():
            return redirect("login")
    else:
        form = user_registration_form()
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
