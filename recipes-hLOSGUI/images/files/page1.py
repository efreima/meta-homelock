# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from typing import Counter
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
import threading
import os
import json
def return_pass():
    with open('config.txt', 'r') as reader:
        data = reader.readlines()
        data = str(data[0])
        return data
def Start():
        os.system("python page2.py")
def Start2():
        os.system("python page3.py") 

Count=0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lockStatus = QtWidgets.QLabel(self.centralwidget)
        self.lockStatus.setGeometry(QtCore.QRect(340, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(10)
        self.lockStatus.setFont(font)
        self.lockStatus.setObjectName("lockStatus")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.door = QtWidgets.QPushButton(self.centralwidget)
        self.door.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"background-color: rgb(0, 255, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}")
        self.door.setObjectName("door")
        self.gridLayout.addWidget(self.door, 1, 1, 1, 1)
        self.device = QtWidgets.QPushButton(self.centralwidget)
        self.device.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"background-color: rgb(0, 255, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}")
        self.device.setObjectName("device")
        self.gridLayout.addWidget(self.device, 4, 0, 1, 1)
        self.lockStatus = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(10)
        self.lockStatus.setFont(font)
        self.lockStatus.setObjectName("lockStatus")
        self.gridLayout.addWidget(self.lockStatus, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.network = QtWidgets.QPushButton(self.centralwidget)
        self.network.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"background-color: rgb(0, 255, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}")
        self.network.setObjectName("network")
        self.gridLayout.addWidget(self.network, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(548, 410))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Capture (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1837, 39))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.door.clicked.connect(self.changeStatus)
        self.device.clicked.connect(self.redirect_password)
        self.network.clicked.connect(self.redirect_password2)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.door.setText(_translate("MainWindow", "Press to Lock/Unlock"))
        self.device.setText(_translate("MainWindow", "Device Control"))
        self.lockStatus.setText(_translate("MainWindow", " "))
        self.network.setText(_translate("MainWindow", "Network Monitor"))

    def updateStatus(self):
        self.lockStatus.setText("What door")
               


    def changeStatus(self):
            f = open('statuses.json' , 'r')
            data = json.load(f)
            status = data["lock"]["locked"]
            f.close()
            dictionary_lock ={
    "name": "Lock Information",
    "description": "Information on the current status of the lock/homelockOS",
    "version": "0.0.0",
    "private": 1,
    "author": "Anonymous",
    "contributors": [ "Someone" ],
    "lock": {
      "locked": 1,
      "canlock": 0
    }

}
            dictionary_unlock ={
    "name": "Lock Information",
    "description": "Information on the current status of the lock/homelockOS",
    "version": "0.0.0",
    "private": 1,
    "author": "Anonymous",
    "contributors": [ "Someone" ],
    "lock": {
      "locked": 0,
      "canlock": 0
    }

}
            json_lock = json.dumps(dictionary_lock, indent = 4)
            json_unlock = json.dumps(dictionary_unlock, indent = 4)
            if status == 1:
                    f = open('statuses.json' , 'w')
                    f.write(json_unlock)
                    f.close()
            else:
                    f = open('statuses.json' , 'w')
                    f.write(json_lock)
                    f.close()
                    
    
    
    def redirect_password(self):
            import subprocess, os
            #subprocess.Popen(['matchbox-keyboard'])
            text, ok = QtWidgets.QInputDialog.getText(None, "Attention", "Enter Password: ", 
            QtWidgets.QLineEdit.Password)
            if ok and text:
                    user_pass = str(text).strip()
            
                    if user_pass == return_pass():
                            Start()
                    else:
                            self.redirect_password()
    def redirect_password2(self):
            import subprocess, os
            #subprocess.Popen(['matchbox-keyboard'])
            text, ok = QtWidgets.QInputDialog.getText(None, "Attention", "Enter Password: ", 
            QtWidgets.QLineEdit.Password)
            if ok and text:
                    user_pass = str(text).strip()
            
                    if user_pass == return_pass():
                            Start2()
                    else:
                            self.redirect_password()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.updateStatus()
    sys.exit(app.exec_())
