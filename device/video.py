from email.quoprimime import body_check
import cv2
import sys
from PIL import Image
import torch
from facenet_pytorch import MTCNN
import numpy as np


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
mtcnn = MTCNN(margin=40, keep_all=True, device=device,post_process=False)
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    boxes,probs = mtcnn.detect(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    


    if boxes is not None:

        filterProbs = probs > 0.90

        boxes = boxes[filterProbs]
    

        for (x, y, w, h) in boxes:
            cv2.rectangle(frame,(round(x),round(y)), (round(w),round(h)),
                        (255, 0, 0),
                        3)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
