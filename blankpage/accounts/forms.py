from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from accounts.models import UserProfile

__author__ = 'Abrar'



class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30,required=True,min_length=5)
    email = forms.EmailField(max_length=30,required=True)
    password1 = forms.CharField(max_length=30,required=True,widget=PasswordInput(),min_length=8,label="Password")
    password2 = forms.CharField(max_length=30,required=True,widget=PasswordInput(),min_length=8,label="Re Enter Password")
    captcha = CaptchaField()


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1","")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password1

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            user = User.objects.get(username = username)
            raise forms.ValidationError("This username is already taken")
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("This email address already exists. Did you forget your password?")
        except User.DoesNotExist:
            return email

    def save(self,new_data):
        u  = User.objects.create_user(new_data["username"],new_data["email"], new_data["password1"])
        u.is_active = True
        u.save()
        profile =  UserProfile()
        profile.user = u
        profile.save()
        return u

class LoginForm(forms.Form):
    username = forms.CharField(required=True,max_length=30)
    password = forms.CharField(required=True,max_length=30,widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        if username =="":
            raise forms.ValidationError("Username must be Specidied")
        return username


    def clean_password(self):
        password = self.cleaned_data['password']
        if password == "":
            raise forms.ValidationError("Password must entered")
        return password