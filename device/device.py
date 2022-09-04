from cgi import test
from email.mime import image
import os
from scipy.spatial.distance import cosine
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
import cv2
import PIL
import torchvision.transforms as transform
from facenet_pytorch import MTCNN
import torch
import numpy as np
class Device:

    def __init__(self) -> None:
        
        self.classifiers = { } #{name: embedding}

        self.deviceIsOn = True

        self.torchdevice = device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.cascade = MTCNN(image_size = 224,margin=40,device=device,post_process=False)


        self.model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')

    def getEmbedding(self,imagePath,extractFace = False):


        img = cv2.imread(imagePath)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        frame = PIL.Image.fromarray(img)
        """
        extractFace = True if the face has not been extracted
        """

        if extractFace:
            face = (self.cascade.forward(frame)).permute(1,2,0).int().numpy()
        else:
            face = frame.resize((224,224))


        face = np.asarray(face)
        
        sample = [np.asarray(face, 'float32')]
        # prepare the face for the model, e.g. center pixels
        sample = preprocess_input(sample, version=2)
        # perform prediction
        yhat = self.model.predict(sample)

        return yhat


    
    def trainCosine(self,trainingDirectory):

        """

        trainingDirectory should have the next structure


        trainingDirectory/

                nameperson1/
                    person1image
                nameperson2/
                    person2image
                
                ....

                namepersonn/
                    personNimage
        
        """


        for personName in os.listdir(trainingDirectory):

            personPath = f"{trainingDirectory}/{personName}"

            

            
            if os.path.isdir(personPath):
            
                pathPersonImage = personPath + "/" + os.listdir(personPath)[0]

                self.classifiers[personName] = self.getEmbedding(pathPersonImage,extractFace=True)


    def is_match(self,ID_embedding, subject_embedding,thresh=0.4):
        # calculate distance between embeddings
        score = cosine(ID_embedding, subject_embedding)

        if score <= thresh:
            return True
        else:
            return False


    def classifyFace(self,framePath):

        matchFound = False

        subjectEmbedding = self.getEmbedding(framePath,extractFace=True)

        for name, knownEmbedding in self.classifiers.items():

            if self.is_match(knownEmbedding.flatten(),subjectEmbedding.flatten()):

                print(f"La persona en la foto {framePath} es {name}")
                matchFound=True

        if not matchFound:
            print(f"En la foto {framePath} hay un desconocido")




    def checkFaces(self,testingDir):
        

        if os.path.isdir(testingDir):

            for image in os.listdir(testingDir):

                imagePath = testingDir + "/" + image
                self.classifyFace(imagePath)










            






a = Device()

a.trainCosine("train_dir")

a.checkFaces("test_dir")



