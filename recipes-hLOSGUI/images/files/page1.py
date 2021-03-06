# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Counter
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import os
import json
import time

def return_pass():
    with open('/usr/share/hLOSGUI/config.txt', 'r') as reader:
        data = reader.readlines()
        data = str(data[0])
        return data
def Start():
        MainWindow.close()
        os.system("python3 /usr/share/hLOSGUI/page2.py")
def Start2():
        MainWindow.close()
        os.system("python3 /usr/share/hLOSGUI/page3.py") 



Count=0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.network = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.network.sizePolicy().hasHeightForWidth())
        self.network.setSizePolicy(sizePolicy)
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
        self.gridLayout.addWidget(self.network, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(250, 50, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(10)
        self.device = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device.sizePolicy().hasHeightForWidth())
        self.device.setSizePolicy(sizePolicy)
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
        self.gridLayout.addWidget(self.device, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(250, 50, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.door = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.door.sizePolicy().hasHeightForWidth())
        self.door.setSizePolicy(sizePolicy)
        self.door.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"font-size: 44px;\n"
"font-style: bold;\n"
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
        self.gridLayout.addWidget(self.door, 1, 1, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1753, 39))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.door.clicked.connect(self.changeStatus)
        self.device.clicked.connect(self.redirect_password)
        self.network.clicked.connect(self.redirect_password2)
        self.pushButton.clicked.connect(self.configure)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.network.setText(_translate("MainWindow", "Network Monitor"))
        self.device.setText(_translate("MainWindow", "Device Control"))
        self.door.setText(_translate("MainWindow", " "))
        self.pushButton.setText(_translate("MainWindow", "Configure"))


    def changeStatus(self):
            f = open('/usr/share/hLOSGUI/statuses.json' , 'r')
            data = json.load(f)
            status = data["locked"]
            f.close()
            dictionary_lock ={
    "locked": 1,
    "canlock": 0
}
            dictionary_unlock ={
    "locked": 0,
    "canlock": 0
}       
            json_lock = json.dumps(dictionary_lock, indent = 4)
            json_unlock = json.dumps(dictionary_unlock, indent = 4)
            if status == 1:
                    f = open('/usr/share/hLOSGUI/statuses.json' , 'w')
                    f.write(json_unlock)
                    f.close()
            else:
                    f = open('/usr/share/hLOSGUI/statuses.json' , 'w')
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


    def configure(self):
            import subprocess, os
            text, ok = QtWidgets.QInputDialog.getText(None, "Configure", "Door Lock IP Address: ",
            QtWidgets.QLineEdit.Normal)
            if ok and text:
                    f = open('/usr/share/hLOSGUI/config/door-server.txt' , 'w')
                    f.write(text)
                    f.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    def updateLabel():
        f1 = open('/usr/share/hLOSGUI/statuses.json' , 'r')
        data1 = json.load(f1)
        status1 = data1['locked']
        f1.close()
        if status1 == 1:
            ui.door.setText("Unlock Door")

        else:
            ui.door.setText("Lock Door")

    timer = QtCore.QTimer()
    timer.timeout.connect(updateLabel)
    timer.start(500)
    sys.exit(app.exec_())
