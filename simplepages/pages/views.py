from django.shortcuts import render
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