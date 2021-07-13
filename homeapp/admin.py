from django.contrib import admin
from .models import Homework, form
# Register your models here.

# @admin.register(image)
# # class ImageAdmin(admin.ModelAdmin):
# #     # list_display = ['id','photo']
admin.site.register(Homework)
admin.site.register(form)