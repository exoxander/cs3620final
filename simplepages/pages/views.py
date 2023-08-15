from django.shortcuts import render, redirect
from .models import Profile, Post
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
        pst_name = request.POST["post_name"]
        pst_description = request.POST["post_description"]
        #p_image = request.POST["post_description"]

        pfl = Profile.objects.get(user=request.user.id)

        #create new post
        Post.objects.create(profile=pfl,postname=pst_name,postdescription=pst_description)

        return redirect("profileredirect")

    return render(request,"pages/postupsert.html")

def profile_redirect(request):
    p = Profile.objects.get(user=request.user.id).id
    
    if(p != None):
        return redirect("profile",profile_id=p)

    return redirect("home")