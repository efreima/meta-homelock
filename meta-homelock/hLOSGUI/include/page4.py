# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nick = QtWidgets.QComboBox(self.centralwidget)
        self.nick.setGeometry(QtCore.QRect(30, 40, 121, 22))
        self.nick.setObjectName("nick")
        self.nick.addItem("")
        self.nick.addItem("")
        self.nick.addItem("")
        self.nick.addItem("")
        self.nick_2 = QtWidgets.QComboBox(self.centralwidget)
        self.nick_2.setGeometry(QtCore.QRect(30, 110, 121, 22))
        self.nick_2.setObjectName("nick_2")
        self.nick_2.addItem("")
        self.nick_2.addItem("")
        self.nick_2.addItem("")
        self.nick_2.addItem("")
        self.nick_3 = QtWidgets.QComboBox(self.centralwidget)
        self.nick_3.setGeometry(QtCore.QRect(30, 180, 121, 22))
        self.nick_3.setObjectName("nick_3")
        self.nick_3.addItem("")
        self.nick_3.addItem("")
        self.nick_3.addItem("")
        self.nick_3.addItem("")
        self.ip = QtWidgets.QComboBox(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(210, 40, 131, 22))
        self.ip.setObjectName("ip")
        self.ip.addItem("")
        self.ip.addItem("")
        self.ip.addItem("")
        self.ip.addItem("")
        self.ip_2 = QtWidgets.QComboBox(self.centralwidget)
        self.ip_2.setGeometry(QtCore.QRect(210, 110, 131, 22))
        self.ip_2.setObjectName("ip_2")
        self.ip_2.addItem("")
        self.ip_2.addItem("")
        self.ip_2.addItem("")
        self.ip_2.addItem("")
        self.ip_3 = QtWidgets.QComboBox(self.centralwidget)
        self.ip_3.setGeometry(QtCore.QRect(210, 180, 131, 22))
        self.ip_3.setObjectName("ip_3")
        self.ip_3.addItem("")
        self.ip_3.addItem("")
        self.ip_3.addItem("")
        self.ip_3.addItem("")
        self.profile = QtWidgets.QComboBox(self.centralwidget)
        self.profile.setGeometry(QtCore.QRect(410, 40, 131, 22))
        self.profile.setObjectName("profile")
        self.profile.addItem("")
        self.profile.addItem("")
        self.profile.addItem("")
        self.profile.addItem("")
        self.profile_2 = QtWidgets.QComboBox(self.centralwidget)
        self.profile_2.setGeometry(QtCore.QRect(410, 110, 131, 22))
        self.profile_2.setObjectName("profile_2")
        self.profile_2.addItem("")
        self.profile_2.addItem("")
        self.profile_2.addItem("")
        self.profile_2.addItem("")
        self.profile_3 = QtWidgets.QComboBox(self.centralwidget)
        self.profile_3.setGeometry(QtCore.QRect(410, 180, 131, 22))
        self.profile_3.setObjectName("profile_3")
        self.profile_3.addItem("")
        self.profile_3.addItem("")
        self.profile_3.addItem("")
        self.profile_3.addItem("")
        self.allow = QtWidgets.QRadioButton(self.centralwidget)
        self.allow.setGeometry(QtCore.QRect(570, 40, 91, 17))
        self.allow.setObjectName("allow")
        self.allow_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.allow_2.setGeometry(QtCore.QRect(570, 110, 91, 17))
        self.allow_2.setObjectName("allow_2")
        self.allow_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.allow_3.setGeometry(QtCore.QRect(570, 180, 91, 17))
        self.allow_3.setObjectName("allow_3")
        self.deny = QtWidgets.QRadioButton(self.centralwidget)
        self.deny.setGeometry(QtCore.QRect(690, 40, 91, 17))
        self.deny.setObjectName("deny")
        self.deny_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.deny_2.setGeometry(QtCore.QRect(690, 110, 91, 17))
        self.deny_2.setObjectName("deny_2")
        self.deny_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.deny_3.setGeometry(QtCore.QRect(690, 180, 91, 17))
        self.deny_3.setObjectName("deny_3")
        self.main = QtWidgets.QPushButton(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(30, 390, 111, 41))
        self.main.setStyleSheet("QPushButton {\n"
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
        self.main.setObjectName("main")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(630, 400, 161, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Capture (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nick.setItemText(0, _translate("MainWindow", "Nickname"))
        self.nick.setItemText(1, _translate("MainWindow", "Nickname1"))
        self.nick.setItemText(2, _translate("MainWindow", "Nickname2"))
        self.nick.setItemText(3, _translate("MainWindow", "Nickname3"))
        self.nick_2.setItemText(0, _translate("MainWindow", "Nickname"))
        self.nick_2.setItemText(1, _translate("MainWindow", "Nickname1"))
        self.nick_2.setItemText(2, _translate("MainWindow", "Nickname2"))
        self.nick_2.setItemText(3, _translate("MainWindow", "Nickname3"))
        self.nick_3.setItemText(0, _translate("MainWindow", "Nickname"))
        self.nick_3.setItemText(1, _translate("MainWindow", "Nickname1"))
        self.nick_3.setItemText(2, _translate("MainWindow", "Nickname2"))
        self.nick_3.setItemText(3, _translate("MainWindow", "Nickname3"))
        self.ip.setItemText(0, _translate("MainWindow", "IP ADDRESS"))
        self.ip.setItemText(1, _translate("MainWindow", "IP ADDRESS 1"))
        self.ip.setItemText(2, _translate("MainWindow", "IP ADDRESS 2"))
        self.ip.setItemText(3, _translate("MainWindow", "IP ADDRESS 3"))
        self.ip_2.setItemText(0, _translate("MainWindow", "IP ADDRESS"))
        self.ip_2.setItemText(1, _translate("MainWindow", "IP ADDRESS 1"))
        self.ip_2.setItemText(2, _translate("MainWindow", "IP ADDRESS 2"))
        self.ip_2.setItemText(3, _translate("MainWindow", "IP ADDRESS 3"))
        self.ip_3.setItemText(0, _translate("MainWindow", "IP ADDRESS"))
        self.ip_3.setItemText(1, _translate("MainWindow", "IP ADDRESS 1"))
        self.ip_3.setItemText(2, _translate("MainWindow", "IP ADDRESS 2"))
        self.ip_3.setItemText(3, _translate("MainWindow", "IP ADDRESS 3"))
        self.profile.setItemText(0, _translate("MainWindow", "Restriction Profile"))
        self.profile.setItemText(1, _translate("MainWindow", "Restriction Profile 1"))
        self.profile.setItemText(2, _translate("MainWindow", "Restriction Profile 2"))
        self.profile.setItemText(3, _translate("MainWindow", "Restriction Profile 3"))
        self.profile_2.setItemText(0, _translate("MainWindow", "Restriction Profile"))
        self.profile_2.setItemText(1, _translate("MainWindow", "Restriction Profile 1"))
        self.profile_2.setItemText(2, _translate("MainWindow", "Restriction Profile 2"))
        self.profile_2.setItemText(3, _translate("MainWindow", "Restriction Profile 3"))
        self.profile_3.setItemText(0, _translate("MainWindow", "Restriction Profile"))
        self.profile_3.setItemText(1, _translate("MainWindow", "Restriction Profile 1"))
        self.profile_3.setItemText(2, _translate("MainWindow", "Restriction Profile 2"))
        self.profile_3.setItemText(3, _translate("MainWindow", "Restriction Profile 3"))
        self.allow.setText(_translate("MainWindow", "Allow Override"))
        self.allow_2.setText(_translate("MainWindow", "Allow Override"))
        self.allow_3.setText(_translate("MainWindow", "Allow Override"))
        self.deny.setText(_translate("MainWindow", "Deny Override"))
        self.deny_2.setText(_translate("MainWindow", "Deny Override"))
        self.deny_3.setText(_translate("MainWindow", "Deny Override"))
        self.main.setText(_translate("MainWindow", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
