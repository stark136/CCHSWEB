from django.contrib import admin
from django.urls import path, include
from homeapp import views
urlpatterns = [
    path('' , views.index, name='home'),
    path('homework' , views.homework, name='home'),
    path('about' , views.about, name='home'),
    path('contact' , views.contact, name='home'),

]
