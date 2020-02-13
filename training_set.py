import os
import cv2
import numpy as np
from PIL import Image




def getImagesWithID(path):
    imageFolders = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []
    for imageFolder in imageFolders:
        imagePaths = [os.path.join(imageFolder, f) for f in os.listdir(imageFolder)]
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNP = np.array(faceImg, 'uint8')
            faces.append(faceNP)
            id = int(os.path.split(imagePath)[-1].split('.')[1])
            ids.append(id)
            cv2.imshow('Training', faceNP)
            cv2.waitKey(10)

    return ids, faces


def training_set():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = './Dataset'
    ids, faces = getImagesWithID(path)
    recognizer.train(faces, np.array(ids))
    if not os.path.exists('./recognizer'):
        os.makedirs('./recognizer')
    recognizer.save('./recognizer/trainingData.yml')
    cv2.destroyAllWindows()
