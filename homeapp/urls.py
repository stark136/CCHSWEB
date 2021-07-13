from django.contrib import admin
from django.urls import path, include
from homeapp import views

admin.sites.AdminSite.site_header = 'Christ Chruch High School Admin Portal'
admin.sites.AdminSite.site_title = 'welcome to cchs admin'
admin.sites.AdminSite.index_title = 'cchs admin page'

urlpatterns = [
    path('' , views.index, name='home'),
    path('homework' , views.homework, name='home'),
    path('about' , views.about, name='home'),
    path('contact' , views.contact, name='home'),

]
