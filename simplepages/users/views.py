from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if(request.method == "POST"):        
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "users/register.html",{"form":form})

def login(request):
    if(request.method == "POST"):        
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, "users/login.html",{"form":form})
