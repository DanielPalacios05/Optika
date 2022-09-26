import cv2
import sys
from PIL import Image
import torch
from facenet_pytorch import MTCNN
import numpy as np
from device import OptikaDevice


#Creo dispositivo

device = OptikaDevice()

device.loadPeople('train_dir')

#Empiezo a cargar las personas conocidas

device.turnCameraON()