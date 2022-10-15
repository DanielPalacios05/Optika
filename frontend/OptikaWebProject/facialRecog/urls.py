from django.urls import path
from . import views


urlpatterns = [
    path('api/blobHandle',views.generateDetectionLog)
]
