from django import forms
from .models import Homework

class ImageForm(forms.ModelForm):
    class Meta():
        model = Homework
        fields =("name","subject", "photo") 
        labels = {'photo':''}