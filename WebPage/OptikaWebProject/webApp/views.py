from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os, sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

path = os.path.join(os.path.dirname(__file__), 'optika-6e7bd-firebase-adminsdk-1c4j0-e8dba28093.json')

# setting up firebase
cred = credentials.Certificate(path)
app = firebase_admin.initialize_app(cred)
db = firebase_admin.firestore.client()


def home(request):
    return render(request, 'home.html')

def peopleToRecog(request):
    return render(request, 'peopleToRecog.html') 

def mainPage(request):  
    return render(request, 'mainPage.html')

def addPerson(request):
    return render(request, 'addPerson.html')

def liveCam(request):
    return render(request, 'liveCam.html')

def detections(request):
    detections_ref = db.collection(u'Detections')
    docs = detections_ref.stream()
    detections = []
    for doc in docs:
        doc_dict = doc.to_dict()
        doc_dict['id'] = doc.id
        detections.append(doc_dict)
    return render(request, 'detections.html', {'detections': detections})
