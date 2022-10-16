from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from azure.storage.blob import BlobClient
from facialrecognition import FacialRecog
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import Twin, TwinProperties


# Create your views here.
facialRecognizer = FacialRecog()


connect_str = "DefaultEndpointsProtocol=https;AccountName=optikaimages;AccountKey=nrYz2nK08cwrcAD3m+7OCxk0ZGLALyVJHECVkdGJlpIpvkaQxIw3E/4iO3CxO01plBfdHcv1Mofq+AStcq9kMg==;EndpointSuffix=core.windows.net"
IOTHUB_CONNECTION_STRING = "HostName=Optika.azure-devices.net;DeviceId=device-1;SharedAccessKey=5MN5TVmcpk6HW/dPOyYWryhuiEKNWnFSnTvLTbUVAuw="
DEVICE_ID = "device-1"

count = 0


@csrf_exempt
def generateDetectionLog(request):

    count+=1

    twin = iothub_registry_manager.get_twin(DEVICE_ID)
    twin_patch = Twin(properties= TwinProperties(desired={'readyToSend' : False}))
    twin = iothub_registry_manager.update_twin(DEVICE_ID, twin_patch, twin.etag)

    blob = BlobClient.from_connection_string(connect_str,"device-upload","device-1/frame.jpg")

    creationDate = blob.get_blob_properties().creation_time

    print(creationDate)

    frame = blob.download_blob().readall()

    print(request.body)

    data = json.loads(request.body)

    print(data)


    iothub_registry_manager = IoTHubRegistryManager(IOTHUB_CONNECTION_STRING)


    twin = iothub_registry_manager.get_twin(DEVICE_ID)
    twin_patch = Twin(properties= TwinProperties(desired={'readyToSend' : True}))
    twin = iothub_registry_manager.update_twin(DEVICE_ID, twin_patch, twin.etag)

    print("veces imagen procesada",count)


    
    return JsonResponse({ "status": 200, "body": {}})
