import os
import dlib
import cv2
import sqlite3
import openface
import training_set

def insertorUpdate(id, name, roll):
    connect = sqlite3.connect('Facial_Recog/Personal_project/recognizer/Face-Database.db')
    cmd = "SELECT * FROM STUDENTS WHERE ID = " + id
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if isRecordExist == 1:
        connect.execute("UPDATE STUDENTS SET NAME = ? WHERE ID = ?", (name, id))
        connect.execute("UPDATE STUDENTS SET ROLL = ? WHERE ID = ?", (roll, id))
    else:
        params = (id, name, roll)
        connect.execute("INSERT INTO STUDENTS VALUES(?, ?, ?)", params)
    connect.commit()
    connect.close()

def dataset_creator(id, name, roll):
    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()
    predictor_model = 'shape_predictor_68_face_landmarks.dat'
    face_aligner = openface.AlignDlib(predictor_model)
    imgDim = 96

    insertorUpdate(id, name, roll)

    folderName = "User" + id
    folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Dataset/" + folderName)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

    sampleNum = 0
    while(True):
        ret, frame = cap.read()
        dets = detector(frame, 1)
        for i, d in enumerate(dets):
            sampleNum += 1
            alignedFace = face_aligner.align(imgDim, frame, d, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
            cv2.imwrite(folderPath + "/User." + id + "." + str(sampleNum) + ".jpg", alignedFace)

            cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (255, 0, 0), 4)
        cv2.namedWindow('Detecting Faces', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Detecting Faces', 600, 600)
        cv2.imshow('Detecting Faces', frame)
        cv2.waitKey(1000)
        if (sampleNum >= 20):
            break

    training_set.training_set()
    cap.release()
    cv2.destroyAllWindows()