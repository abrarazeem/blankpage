from django.forms import forms, ModelForm
from accounts.models import *
__author__ = 'Abrar'


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude= ('user',)

class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude= ('user',)

class WorkForm(ModelForm):
    class Meta:
        model = Work
        exclude= ('user',)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude= ('user',)

class EmailForm(ModelForm):
    class Meta:
        model = EmailAccount
        exclude= ('user','status',)

class ImForm(ModelForm):
    class Meta:
        model = ImAccount
        exclude= ('user','status',)

class MobileForm(ModelForm):
    class Meta:
        model = MobileAccount
        exclude= ('user','status',)
