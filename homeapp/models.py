from django.db import models
from django.db.models.fields import DateTimeField
from django.db import models
# Create your models here.
class Homework(models.Model):
    name = models.CharField(max_length=50, default="")
    subject=models.CharField(max_length=50 , default="")
    photo= models.ImageField(upload_to="Homeworks")
    # date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + ":---" + self.subject

