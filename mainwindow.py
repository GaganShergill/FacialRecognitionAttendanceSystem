# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from insertdialog import Ui_InsertDialog
from camdialog_main import camdialog
import spreadsheet
import subprocess

class Ui_MainWindow(object):
    def openCamWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = camdialog()

    def openInsertWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InsertDialog()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 511)
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 591, 71))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 360, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_date_time = QtWidgets.QLabel(self.centralWidget)
        self.label_date_time.setGeometry(QtCore.QRect(200, 60, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_date_time.setFont(font)
        self.label_date_time.setText("")
        self.label_date_time.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_date_time.setObjectName("label_date_time")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 160, 300, 160))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_1.setObjectName("radioButton_1")
        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionInsert_Update = QtWidgets.QAction(MainWindow)
        self.actionInsert_Update.setObjectName("actionInsert_Update")
        self.actionTake_Attendance_2 = QtWidgets.QAction(MainWindow)
        self.actionTake_Attendance_2.setObjectName("actionTake_Attendance_2")
        self.actionView_Attendance_Sheet = QtWidgets.QAction(MainWindow)
        self.actionView_Attendance_Sheet.setObjectName("actionView_Attendance_Sheet")
        self.actionClass_Information = QtWidgets.QAction(MainWindow)
        self.actionClass_Information.setObjectName("actionClass_Information")


        self.retranslateUi(MainWindow)
        self.radioButton.setChecked(True)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def on_pushButton_clicked(self):
        if self.radioButton.isChecked():
            self.openInsertWindow()
        if self.radioButton_1.isChecked():
            self.openCamWindow()
        if self.radioButton_2.isChecked():
            spreadsheet.create_spreadsheet()
            proc = subprocess.Popen(['soffice', 'reports.xlsx'])
            proc.wait()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Facial Recognition System"))
        self.label.setText(_translate("MainWindow", "Attendance System Based on Facial Recognition"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.radioButton.setText(_translate("MainWindow", "Insert/Update Student\'s Information"))
        self.radioButton_1.setText(_translate("MainWindow", "Take Attendance"))
        self.radioButton_2.setText(_translate("MainWindow", "Class Information "))
        self.actionInsert_Update.setText(_translate("MainWindow", "Insert/Update Student\'s Information"))
        self.actionTake_Attendance_2.setText(_translate("MainWindow", "Take Attendance"))
        self.actionView_Attendance_Sheet.setText(_translate("MainWindow", "View Attendance Sheet"))
        self.actionClass_Information.setText(_translate("MainWindow", "Class Information "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

