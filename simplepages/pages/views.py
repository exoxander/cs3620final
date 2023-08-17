import profile
from django.shortcuts import render, redirect
from .models import Profile, Post
from .forms import *
from random import randint
from django.contrib.auth.models import User

# Create your views here.
def home(request):

    profile_count = Profile.objects.all().count()
    #grab 3 random users from database
    profile_list = []

    i=0
    while(i < 3):

        random_profile = Profile.objects.get(pk=randint(1,profile_count))

        if(random_profile != None):
            profile_list.append(random_profile)
            i = i + 1
        
    return render(request, "pages/home.html",{"profile_list":profile_list})

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
        form = post_upsert_form(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect("profileredirect")

    form = post_upsert_form()
    profileid = Profile.objects.get(user=request.user.id).id
    return render(request,"pages/postupsert.html",{"form":form,"profileid":profileid})

def profile_redirect(request):
    p = Profile.objects.get(user=request.user.id).id
    
    if(p != None):
        return redirect("profile",profile_id=p)

    return redirect("home")

def search_post_filter(request, filter):
    return Post.objects.filter(postname__contains=filter)

def search_profile_filter(request, filter):
    return Profile.objects.filter(user__username__contains=filter)

def search(request):

    searchvalue = "Search"
    profile_list = Profile.objects.all()
    post_list = Post.objects.all()

    if(request.method == "POST"):
        profile_list = search_profile_filter(request,request.POST["search"])
        post_list = search_post_filter(request,request.POST["search"])
        searchvalue = request.POST["search"]

    return render(request, "pages/search.html",{"profile_list":profile_list,"post_list":post_list,"searchvalue":searchvalue})

def post_details(request, post_id):
    selected_post = Post.objects.get(pk=post_id)

    return render(request,"pages/postdetails.html",{"post":selected_post})

def user_update(request):
    if(request.method=="POST"):
        form = user_update_form(request.POST)
        if(form.is_valid()):
            changed_user = User.objects.get(pk=request.user.id)

            changed_user.first_name = request.POST["first_name"]
            changed_user.last_name = request.POST["last_name"]

            changed_user.save()
            return redirect("profileredirect")
    
    userid = request.user.id
    form = user_update_form()
    return render(request,"pages/userupdate.html",{"form":form})


def profile_update(request):
    
    if(request.method == "POST"):
        form = profile_update_form(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect("profileredirect")

    p = Profile.objects.get(user=request.user.id)
    form = profile_update_form(instance=p)
    return render(request,"pages/profileupdate.html",{"form":form})




            #form.clean()
            #changed_profile = Profile.objects.get(user=request.user.id)
            #
            #changed_profile.aboutme = request.POST["aboutme"]
            #changed_profile.image = form.cleaned_data["profileimage"]
            #
            #changed_profile.save()