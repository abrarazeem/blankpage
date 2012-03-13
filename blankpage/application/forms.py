from django import forms

__author__ = 'Abrar'
from django.forms import ModelForm
from piston.models import Consumer



class ApplicationForm(ModelForm):
    name = forms.CharField(max_length=255,required=True,label = "Application Name")
    description = forms.CharField(required=True,widget = forms.Textarea(),label="Application Description")
    class Meta:
        model = Consumer
        fields = ('name','description')


    def save(self,new_data,user):
        c = Consumer()
        c.name = new_data['name']
        c.description = new_data['description']
        c.user = user
        c.status = 'accepted'
        c.generate_random_codes()
        return c