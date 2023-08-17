from django import forms
from .models import Post, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class post_upsert_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["profile","postname","postdescription","postimage"]

class profile_update_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields=["aboutme","profileimage"]

class user_update_form(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name","last_name"]

class post_create_form(forms.Form):
    name = forms.CharField(label="Title",max_length=100)
    desc = forms.CharField(label="Description",max_length=2048)
    img = forms.ImageField(label="Image")

    def clean(self):
        cleaned_data = super().clean()