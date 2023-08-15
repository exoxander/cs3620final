from django.shortcuts import render, redirect
from .models import Profile, Post
from .forms import post_create_form
from .forms import post_upsert_form
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,"pages/home.html",{})

def page_profile(request, profile_id):

    if(profile_id is not None):
        profile_page = Profile.objects.get(pk=profile_id)
        profile_user = User.objects.get(pk=profile_page.user.id)
        profile_posts = Post.objects.all().filter(profile=profile_page.id)

        context={"profile_page":profile_page,"profile_user":profile_user,"profile_posts":profile_posts}

        return render(request,"pages/profile.html",context)

    return render(request,"pages/home.html",{})

def post_upsert(request):  

    if(request.method == "POST"):
        form = post_upsert_form(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()

        return redirect("profileredirect")

    form = post_upsert_form()

    return render(request,"pages/postupsert.html",{"form":form})

def profile_redirect(request):
    p = Profile.objects.get(user=request.user.id).id
    
    if(p != None):
        return redirect("profile",profile_id=p)

    return redirect("home")