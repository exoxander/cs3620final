from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileimage = models.ImageField(upload_to="profileimages", default="NotFound.jpg")
    aboutme = models.CharField(max_length=1024, default="No Information")

    def __str__(self):
        return self.user.username

class Post(models.Model):
    postname = models.CharField(max_length=20)
    postdescription = models.CharField(max_length=2048)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    postimage = models.ImageField(upload_to="postimages", default="NotFound.jpg")

    def __str__(self):
        return self.postname


class comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    commentdata = models.CharField(max_length=128)