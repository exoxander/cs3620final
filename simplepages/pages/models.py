from django.db import models

class profile(models.Model):

    user = models.ForeignKey(models.User, on_delete=models.CASCADE)
    profileimage = models.ImageField(upload_to="profileimages", default="profileimages/default.jpg")

class post(models.Model):
    postname = models.CharField(max_length=20)
    postdescription = models.CharField(max_length=2048)

    user = models.ForeignKey(models.User, on_delete=models.CASCADE)

    postimage = models.ImageField(upload_to="postimages", default="postimages/default.jpg")


class comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(models.User, on_delete=models.CASCADE)

    commentdata = models.CharField(max_length=128)