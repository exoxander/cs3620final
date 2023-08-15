from django import forms
from .models import Post

class post_upsert_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["profile","postname","postdescription","postimage"]

class post_create_form(forms.Form):
    name = forms.CharField(label="Title",max_length=100)
    desc = forms.CharField(label="Description",max_length=2048)
    img = forms.ImageField(label="Image")

    def clean(self):
        cleaned_data = super().clean()