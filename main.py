import sys
import socket
from threading import Thread, Event
from time import sleep
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
My_IP = socket.gethostbyname_ex(socket.gethostname())[-1][-1]


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(960, 512)
        MainWindow1.setMinimumSize(QtCore.QSize(960, 512))
        MainWindow1.setMaximumSize(QtCore.QSize(960, 512))
        MainWindow1.setBaseSize(QtCore.QSize(960, 512))
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 960, 512))
        self.label.setMinimumSize(QtCore.QSize(960, 512))
        self.label.setMaximumSize(QtCore.QSize(960, 512))
        self.label.setBaseSize(QtCore.QSize(960, 512))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image1.png"))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(129, 119, 709, 202))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(320, 180))
        self.pushButton_2.setMaximumSize(QtCore.QSize(320, 180))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mysh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(350, 180))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(320, 180))
        self.pushButton.setMaximumSize(QtCore.QSize(320, 180))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("tachpad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(350, 180))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 320, 460, 90))
        self.pushButton_3.setMinimumSize(QtCore.QSize(400, 90))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Go_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(500, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow1.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow1"))

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(960, 512)
        MainWindow2.setMinimumSize(QtCore.QSize(960, 512))
        MainWindow2.setMaximumSize(QtCore.QSize(960, 512))
        MainWindow2.setBaseSize(QtCore.QSize(960, 512))
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 960, 512))
        self.label.setMinimumSize(QtCore.QSize(960, 512))
        self.label.setMaximumSize(QtCore.QSize(960, 512))
        self.label.setBaseSize(QtCore.QSize(960, 512))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image1.png"))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(129, 119, 709, 202))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(320, 180))
        self.pushButton_2.setMaximumSize(QtCore.QSize(320, 180))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("wifi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(350, 180))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(320, 180))
        self.pushButton.setMaximumSize(QtCore.QSize(320, 180))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("usb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(350, 180))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 320, 460, 90))
        self.pushButton_3.setMinimumSize(QtCore.QSize(400, 90))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(500, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow2"))

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(960, 512)
        MainWindow3.setMinimumSize(QtCore.QSize(960, 512))
        MainWindow3.setMaximumSize(QtCore.QSize(960, 512))
        MainWindow3.setBaseSize(QtCore.QSize(960, 512))
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 960, 512))
        self.label.setMinimumSize(QtCore.QSize(960, 512))
        self.label.setMaximumSize(QtCore.QSize(960, 512))
        self.label.setBaseSize(QtCore.QSize(960, 512))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image1.png"))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(129, 119, 711, 202))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(320, 180))
        self.pushButton_2.setMaximumSize(QtCore.QSize(320, 180))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(350, 180))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(320, 180))
        self.pushButton.setMaximumSize(QtCore.QSize(320, 180))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Cond")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(46, 46, 46);")
        self.pushButton.setText(My_IP)
        #self.pushButton.setText("192.168.42.105")
        self.pushButton.setIconSize(QtCore.QSize(350, 180))
        self.pushButton.setShortcut("")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 320, 460, 90))
        self.pushButton_3.setMinimumSize(QtCore.QSize(400, 90))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Go_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(500, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow3.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "MainWindow3"))


class MainWindow1(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.action1)
        self.pushButton_3.clicked.connect(self.action2)

    def action1(self):
        self.mainWindow3 = MainWindow3()
        self.mainWindow3.show()
        self.mainWindow1 = MainWindow1()
        self.close()

    def action2(self):
        self.mainWindow2 = MainWindow2()
        self.mainWindow2.show()
        self.mainWindow1 = MainWindow1()
        self.close()

class MainWindow2(QtWidgets.QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.action1)


    def action1(self):
        self.mainWindow1 = MainWindow1()
        self.mainWindow1.show()
        self.mainWindow2 = MainWindow2()
        self.close()

class MainWindow3(QtWidgets.QMainWindow, Ui_MainWindow3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.action1)


    def action1(self):
        self.mainWindow1 = MainWindow1()
        self.mainWindow1.show()
        self.mainWindow3 = MainWindow3()
        self.close()


def podkluch():
    server.bind((My_IP, 1234))
    # server.listen()
    print(My_IP)
    server.listen()
    while True:
        user, adres = server.accept()
        print("Connected")
        while True:
            data = user.recv(1024).decode("utf-8").lower()
            print(data)

if __name__ == "__main__":
    th1 = Thread(target=podkluch)
    th1.start()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow2()
    w.show()
    sys.exit(app.exec_())

