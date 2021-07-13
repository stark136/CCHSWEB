from django.shortcuts import render, HttpResponse
from .forms import ImageForm
# Create your views here.
def index(request):
    return render(request, "home.html")

def homework(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    return render(request, "homework.html", {'form':form})

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
