from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm


# Create your views here.
# Function for the home page
def index(request):
    return render(request, 'myInApp/index.html')


# Function for the about page
def about(request):
    return render(request, 'myInApp/about.html')


# Function for the gallery page
def gallery(request):
    return render(request, 'myInApp/gallery.html')


# Function for the ressources page
def resources(request):
    return render(request, 'myInApp/resources.html')


# Function for the contacts page
def contacts(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("index")
    else:
        form = ContactForm()
    return render(request, 'myInApp/contacts.html', {"form": form})
