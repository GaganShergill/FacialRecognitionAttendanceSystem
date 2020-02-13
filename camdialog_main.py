import sys
import cv2
from PyQt5.QtWidgets import QDialog, QAction #<<<<---------Modified
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from camdialog import Ui_CamDialog
import time
import os
import recognize_image_dlib
import subprocess

class camdialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CamDialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.quit = QAction("Quit", self) #<<<<<-----------Added
        self.ui.quit.triggered.connect(self.closeEvent) #<<<<<<----------Added
        self.ui.pushButton_2.clicked.connect(self.start_webcam)
        self.ui.pushButton.clicked.connect(self.stop_webcam)
        self.ui.pushButton_3.clicked.connect(self.save_image)
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1366)#<<<<---------Modified
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 768)#<<<<---------Modified
        self.isCapture = False
        self.picNum = 0

    def closeEvent(self, QCloseEvent):#<<<<<<----------Added
        self.capture.release()#<<<<<<----------Added

    def save_image(self):
        if self.timer.isActive():#<<<<<<----------Added
            self.timer.stop()#<<<<<<----------Added
        self.isCapture = True
        self.update_frame()


    def start_webcam(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    def update_frame(self):
        ret, self.image = self.capture.read()
        if ret == True:
            self.displayImage(self.image, 1)
        if self.isCapture == True:
            date = time.strftime("%d.%m.%Y")
            path = './Pics_Taken/' + date
            if not os.path.exists(path):
                os.makedirs(path)
                f = open(path + "/pictureNumber.txt", "w+")
                f.write(str(self.picNum + 1))
                f.close()

            f = open(path + "/pictureNumber.txt", "r")
            self.picNum = int(f.read())
            f.close()
            f = open(path + "/pictureNumber.txt", "w")
            f.write(str(self.picNum + 1))
            f.close()
            cv2.imwrite(path + "/pic" + str(self.picNum) + ".jpg", self.image)
            recognize_image_dlib.recognize_image_dlib(str(self.picNum))
            proc = subprocess.Popen(['soffice', path+'/attendance.xlsx'])
            proc.wait()
            self.isCapture = False


    def stop_webcam(self):
        self.timer.stop()

    def displayImage(self, img, win = 1):
        img = cv2.flip(img, 1)  # <<<<---------Added
        qformat=QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#<<<<<<----------Added
        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        #removed rgbSwapped()
        if win==1:
            self.ui.label.setPixmap(QPixmap.fromImage(outImage))
            self.ui.label.setScaledContents(True)


