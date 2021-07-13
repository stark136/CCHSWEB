from django.shortcuts import render, HttpResponse
from .forms import ImageForm, contact1
from .models import form
# Create your views here.
def index(request):
    return render(request, "home.html")

def homework(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "done.html")
    form = ImageForm()
    return render(request, "homework.html", {'form':form})

def contact(request):
    context={}
    form = contact1(data=request.POST or None)
        # name= request.POST.get('name')
        # email= request.POST.get('email')
        # number= request.POST.get('number')
        # address= request.POST.get('address')
        # a= form(name=name, email=email, number=number, address=address)
        # a.save()
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form']= form
    return render(request, "contact.html", context)
    # return render(request, "contact.html")

def about(request):
    return render(request, "about.html")



