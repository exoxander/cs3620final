from django import forms

class user_registration_form(forms.Form):
    name = forms.CharField(label="Username",max_length=100,)
    pwd1 = forms.CharField(label="Password",max_length=100)
    pwd2 = forms.CharField(label="Confirm Password",max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        cleanedpwd1 = cleaned_data.get("pwd1")
        cleanedpwd2 = cleaned_data.get("pwd2")

        if(cleanedpwd1 != cleanedpwd2):
            self.add_error("pwd2","Passwords Do Not Match")