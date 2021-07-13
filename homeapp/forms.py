from django import forms
from django.db.models import fields
from .models import Homework, form

class ImageForm(forms.ModelForm):
    class Meta():
        model = Homework
        fields =("name","subject", "photo", "date") 
        labels = {'photo':''}

class contact1(forms.ModelForm):
    class Meta():
        model = form
        fields =("__all__")
