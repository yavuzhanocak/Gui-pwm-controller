# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PycharmProjects\pythonProject2\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(455, 270)
        MainWindow.setMinimumSize(QtCore.QSize(200, 270))
        MainWindow.setMaximumSize(QtCore.QSize(455, 288))
        MainWindow.setMouseTracking(False)
        MainWindow.setStatusTip("")
        MainWindow.setStyleSheet("\n"
"background-color:rgb(50, 47, 61);")
        MainWindow.setWindowFilePath("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 451, 270))
        self.groupBox_2.setMinimumSize(QtCore.QSize(450, 270))
        self.groupBox_2.setStyleSheet("background-color:rgb(50, 47, 61);\n"
"border: rgb(50, 47, 61);;\n"
"border-width: 3px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(0, 100, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(31, 52, 41,00);")
        self.label_4.setObjectName("label_4")
        self.comboBoudrate = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoudrate.setGeometry(QtCore.QRect(0, 120, 125, 20))
        self.comboBoudrate.setMinimumSize(QtCore.QSize(125, 0))
        self.comboBoudrate.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
" border-radius: 5px;\n"
"border: 2px solid gray;")
        self.comboBoudrate.setObjectName("comboBoudrate")
        self.comboComport = QtWidgets.QComboBox(self.groupBox_2)
        self.comboComport.setGeometry(QtCore.QRect(0, 60, 125, 20))
        self.comboComport.setMinimumSize(QtCore.QSize(125, 0))
        self.comboComport.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
" border-radius: 5px;\n"
"border: 2px solid gray;")
        self.comboComport.setObjectName("comboComport")
        self.labelComport = QtWidgets.QLabel(self.groupBox_2)
        self.labelComport.setGeometry(QtCore.QRect(0, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelComport.setFont(font)
        self.labelComport.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(31, 52, 41,00);")
        self.labelComport.setObjectName("labelComport")
        self.buttonConnect = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonConnect.setGeometry(QtCore.QRect(130, 10, 121, 31))
        self.buttonConnect.setMinimumSize(QtCore.QSize(100, 25))
        self.buttonConnect.setAccessibleName("")
        self.buttonConnect.setStyleSheet("background-color: rgb(160, 193, 184);\n"
"border: 1px solid gray;\n"
"border-width: 3px;\n"
"border-radius:10px;")
        self.buttonConnect.setObjectName("buttonConnect")
        self.percent = QtWidgets.QRadioButton(self.groupBox_2)
        self.percent.setGeometry(QtCore.QRect(20, 200, 82, 17))
        self.percent.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,00);")
        self.percent.setObjectName("percent")
        self.second = QtWidgets.QRadioButton(self.groupBox_2)
        self.second.setGeometry(QtCore.QRect(20, 180, 82, 17))
        self.second.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,00);")
        self.second.setObjectName("second")
        self.buttonDisconnect = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonDisconnect.setGeometry(QtCore.QRect(270, 10, 121, 31))
        self.buttonDisconnect.setMinimumSize(QtCore.QSize(100, 25))
        self.buttonDisconnect.setStyleSheet("background-color: rgb(160, 193, 184);\n"
"border: 1px solid gray;\n"
"border-width: 3px;\n"
"border-radius:10px;")
        self.buttonDisconnect.setObjectName("buttonDisconnect")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(130, 50, 321, 211))
        self.groupBox.setMinimumSize(QtCore.QSize(300, 200))
        self.groupBox.setStyleSheet("border-radius:10px;\n"
"background-color:rgb(75, 93, 103);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(220, 40, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 170, 127,00);")
        self.label_5.setObjectName("label_5")
        self.comboSecond = QtWidgets.QComboBox(self.groupBox)
        self.comboSecond.setGeometry(QtCore.QRect(220, 100, 64, 20))
        self.comboSecond.setMinimumSize(QtCore.QSize(0, 0))
        self.comboSecond.setMaximumSize(QtCore.QSize(600, 16777215))
        self.comboSecond.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border: 2px solid gray;")
        self.comboSecond.setObjectName("comboSecond")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(56, 75, 65,00);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.buttonSend = QtWidgets.QPushButton(self.groupBox)
        self.buttonSend.setGeometry(QtCore.QRect(40, 140, 200, 60))
        self.buttonSend.setMinimumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buttonSend.setFont(font)
        self.buttonSend.setStyleSheet("background-color:rgb(160, 193, 184);\n"
"border: 1px solid gray;\n"
"border-width: 3px;\n"
"border-radius:10px;\n"
"")
        self.buttonSend.setCheckable(True)
        self.buttonSend.setObjectName("buttonSend")
        self.labelPercent = QtWidgets.QLabel(self.groupBox)
        self.labelPercent.setGeometry(QtCore.QRect(220, 100, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPercent.setFont(font)
        self.labelPercent.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 170, 127,00);")
        self.labelPercent.setObjectName("labelPercent")
        self.lineDutycycle = QtWidgets.QLineEdit(self.groupBox)
        self.lineDutycycle.setGeometry(QtCore.QRect(10, 90, 200, 30))
        self.lineDutycycle.setMinimumSize(QtCore.QSize(200, 30))
        self.lineDutycycle.setStyleSheet("border-color:  rgb(85, 170, 127);\n"
"border: 1px solid gray;\n"
"border-width: 3px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.lineDutycycle.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineDutycycle.setObjectName("lineDutycycle")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 0, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(56, 75, 65,00);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineFrequency = QtWidgets.QLineEdit(self.groupBox)
        self.lineFrequency.setGeometry(QtCore.QRect(10, 30, 200, 30))
        self.lineFrequency.setMinimumSize(QtCore.QSize(200, 30))
        self.lineFrequency.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray;\n"
"border-width: 3px;\n"
"border-radius:10px;")
        self.lineFrequency.setObjectName("lineFrequency")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PWM Controller"))
        self.label_4.setText(_translate("MainWindow", "Baud Rate"))
        self.labelComport.setText(_translate("MainWindow", "Com Port"))
        self.buttonConnect.setText(_translate("MainWindow", "Connect"))
        self.percent.setText(_translate("MainWindow", "Percent"))
        self.second.setText(_translate("MainWindow", "Second"))
        self.buttonDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.label_5.setText(_translate("MainWindow", "Hz"))
        self.label_2.setText(_translate("MainWindow", "Duty Cycle"))
        self.buttonSend.setText(_translate("MainWindow", "Send Data"))
        self.buttonSend.setShortcut(_translate("MainWindow", "Return"))
        self.labelPercent.setText(_translate("MainWindow", "%"))
        self.label.setText(_translate("MainWindow", "Frequency"))
        self.label_7.setText(_translate("MainWindow", "PWM Controller"))

