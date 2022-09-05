from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

# Create your views here.

def home(request):
    return render(request, 'home.html')
