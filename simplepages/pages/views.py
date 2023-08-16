from django.shortcuts import render, redirect
from .models import Profile, Post
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