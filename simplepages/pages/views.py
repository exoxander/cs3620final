from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"pages/home.html",{})

def page_profile(request):
    return render(request,"pages/profile.html",{})