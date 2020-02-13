import cv2
import openface
import dlib
import sqlite3
import numpy as np
import time
from PIL import Image
import attendance



def getProfile(id):
    connect = sqlite3.connect('Facial_Recog/Personal_project/recognizer/Face-Database.db')
    cmd = "SELECT * FROM STUDENTS WHERE ID = " + str(id)
    cursor = connect.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    connect.close()
    return profile


def recognize_image_dlib(picNum):
    detector = dlib.get_frontal_face_detector()
    predictor_model = 'shape_predictor_68_face_landmarks.dat'
    face_aligner = openface.AlignDlib(predictor_model)

    recog = cv2.face.LBPHFaceRecognizer_create()
    recog.read('./recognizer/trainingData.yml')
    font = cv2.FONT_HERSHEY_PLAIN

    date = time.strftime("%d.%m.%Y")
    path = './Pics_Taken/' + date
    imagePath = path + "/pic" + picNum + ".jpg"
    frame = cv2.imread(imagePath)

    dets = detector(frame, 1)
    faceRec = 0
    totalConf = 0.0
    profiles = []
    for i, d in enumerate(dets):
        alignedFace = face_aligner.align(96, frame, d, landmarkIndices= openface.AlignDlib.OUTER_EYES_AND_NOSE)
        cv2.imwrite('forRecog.jpg', alignedFace)
        FaceImg = Image.open('forRecog.jpg').convert('L')
        FaceNP = np.array(FaceImg, 'uint8')
        id, conf = recog.predict(FaceNP)
        if conf > 50 and conf < 100:
            totalConf += conf
            faceRec += 1
            profile = getProfile(id)
            if profile != None:
                profiles.append(profile)
                cv2.putText(frame, profile[1] + str("(%.2f)" % conf),
                            (d.left(), d.bottom()), font, 2.5, (0, 0, 255), 3)
        else:
            cv2.putText(frame, "Unknown",
                        (d.left(), d.bottom()), font, 2.5, (0, 0, 255), 5)

        cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (255,0,0), 2)


    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)
    cv2.waitKey(0)
    detectPrint = " %d face detected" % len(dets)
    if faceRec != 0 :
        print(detectPrint + " and ", faceRec, " face recognized with confidence %.2f"%(totalConf/faceRec))
    else:
        print(detectPrint + " and 0 faces recognized")

    attendance.give_attendance(profiles)
    cv2.destroyAllWindows()

