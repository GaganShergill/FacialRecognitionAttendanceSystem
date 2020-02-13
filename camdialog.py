# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camdialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CamDialog(object):
    def setupUi(self, CamDialog):
        CamDialog.setObjectName("CamDialog")
        CamDialog.resize(1386, 838)#<<<<---------Modified
        self.label = QtWidgets.QLabel(CamDialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 1366, 768))#<<<<---------Modified
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(CamDialog)
        self.widget.setGeometry(QtCore.QRect(10, 6, 1366, 51))#<<<<---------Modified
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.retranslateUi(CamDialog)
        QtCore.QMetaObject.connectSlotsByName(CamDialog)
        CamDialog.setWindowModality(QtCore.Qt.ApplicationModal)

    def retranslateUi(self, CamDialog):
        _translate = QtCore.QCoreApplication.translate
        CamDialog.setWindowTitle(_translate("CamDialog", "Dialog"))
        self.pushButton_2.setText(_translate("CamDialog", "Start WebCam"))
        self.pushButton_3.setText(_translate("CamDialog", "Capture"))
        self.pushButton.setText(_translate("CamDialog", "Stop/Pause"))

