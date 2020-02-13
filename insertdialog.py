# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertdialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import dataset_creator

class Ui_InsertDialog(object):
    def setupUi(self, InsertDialog):
        InsertDialog.setObjectName("InsertDialog")
        InsertDialog.resize(640, 480)
        self.groupBox = QtWidgets.QGroupBox(InsertDialog)
        self.groupBox.setGeometry(QtCore.QRect(70, 50, 511, 321))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(InsertDialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 390, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        self.retranslateUi(InsertDialog)
        QtCore.QMetaObject.connectSlotsByName(InsertDialog)
        InsertDialog.setWindowModality(QtCore.Qt.ApplicationModal)

    def on_pushButton_clicked(self):
        userID = self.lineEdit.text()
        name = self.lineEdit_2.text()
        roll = self.lineEdit_3.text()
        dataset_creator.dataset_creator(userID, name, roll)
        self.pushButton.close()

    def retranslateUi(self, InsertDialog):
        _translate = QtCore.QCoreApplication.translate
        InsertDialog.setWindowTitle(_translate("InsertDialog", "Dialog"))
        self.groupBox.setTitle(_translate("InsertDialog", "Add Information"))
        self.label.setText(_translate("InsertDialog", "User ID:"))
        self.label_2.setText(_translate("InsertDialog", "Name:"))
        self.label_3.setText(_translate("InsertDialog", "Roll Number:"))
        self.pushButton.setText(_translate("InsertDialog", "Submit"))




