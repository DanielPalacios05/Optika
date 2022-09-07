from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

# Create your views here.

def home(request):
    return render(request, 'home.html')

def what(request):
    return render(request, 'what.html')

def why(request):
    return render(request, 'why.html')

def func(request):
    return render(request, 'func.html')

def login(request):
    return render(request, 'login.html')

def peopleToRecog(request):
    return render(request, 'peopleToRecog.html')

def addPerson(request):
    return render(request, 'addPerson.html')
