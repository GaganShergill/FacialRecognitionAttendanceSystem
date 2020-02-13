import cv2
import dlib
import numpy as np


def get_landmarks(im):
    detector = dlib.get_frontal_face_detector()
    PREDICTOR_PATH = "./shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(PREDICTOR_PATH)
    dets = detector(im, 1)
    for i, d in enumerate(dets):
        return np.matrix([[p.x, p.y] for p in predictor(im, d).parts()])


def annotate_landmarks(im, landmarks):
    im = im.copy()
    for idx, point in enumerate(landmarks):
        pos = (point[0, 0], point[0, 1])
        cv2.putText(im, str(idx), pos,
                    fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                    fontScale=0.4,
                    color=(0, 0, 255))
        cv2.circle(im, pos, 3, color=(0, 255, 255))
    return im

def landmark_finding():
    im=cv2.imread('test1.jpg')
    image = annotate_landmarks(im,get_landmarks(im))
    image2 = cv2.resize(image, (1777, 1000))
    cv2.imshow("Result", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    landmark_finding()