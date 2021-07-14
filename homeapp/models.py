from django.db import models
from django.db.models.fields import DateTimeField
from django.db import models
from django.utils import timezone
# Create your models here.
class Homework(models.Model):
    name = models.CharField(max_length=50, default="")
    subject=models.CharField(max_length=50 , default="")
    photo= models.FileField(upload_to="Homeworks")
    date= models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name + ":---" + self.subject 

class form(models.Model):
    name= models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    number=models.CharField(max_length=14, )
    address= models.CharField(max_length=300)
    description = models.TextField(default ="")
    date= models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 
