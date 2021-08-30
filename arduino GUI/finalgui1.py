# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import time
import serial

while True:
    
    try:
        a = input('com port:')
        ard = serial.Serial('com'+a,9600)
        print('success')
        break
    except:
        print('wrong com')


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker,self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        
    @pyqtSlot()
    def run(self):
        '''
        Your code goes in this function
        '''
        self.fn(*self.args, **self.kwargs)


class Ui_MainWindow(object):
    def __init__(self, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 800)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.G_meterValues = QtWidgets.QGroupBox(self.centralwidget)
        self.G_meterValues.setGeometry(QtCore.QRect(400, 60, 1091, 261))
        self.G_meterValues.setObjectName("G_meterValues")
        self.L_meter1v = QtWidgets.QLabel(self.G_meterValues)
        self.L_meter1v.setGeometry(QtCore.QRect(150, 120, 131, 51))
        self.L_meter1v.setStyleSheet("background-color:white;")
        self.L_meter1v.setText("")
        self.L_meter1v.setObjectName("L_meter1v")
        self.L_meter2v = QtWidgets.QLabel(self.G_meterValues)
        self.L_meter2v.setGeometry(QtCore.QRect(420, 120, 131, 51))
        self.L_meter2v.setStyleSheet("background-color:white;")
        self.L_meter2v.setText("")
        self.L_meter2v.setObjectName("L_meter2v")
        self.L_meter3v = QtWidgets.QLabel(self.G_meterValues)
        self.L_meter3v.setGeometry(QtCore.QRect(660, 120, 131, 51))
        self.L_meter3v.setStyleSheet("background-color:white;")
        self.L_meter3v.setText("")
        self.L_meter3v.setObjectName("L_meter3v")
        self.L_meter4v = QtWidgets.QLabel(self.G_meterValues)
        self.L_meter4v.setGeometry(QtCore.QRect(890, 120, 131, 51))
        self.L_meter4v.setStyleSheet("background-color:white;")
        self.L_meter4v.setText("")
        self.L_meter4v.setObjectName("L_meter4v")
        self.L_meter1head = QtWidgets.QLabel(self.G_meterValues)
        self.L_meter1head.setGeometry(QtCore.QRect(150, 80, 131, 41))
        self.L_meter1head.setAlignment(QtCore.Qt.AlignCenter)
        self.L_meter1head.setObjectName("L_meter1head")
        self.L_meter2head = QtWidgets.QLabel(self.G_meterValues)
        self.L_meter2head.setGeometry(QtCore.QRect(420, 80, 131, 41))
        self.L_meter2head.setAlignment(QtCore.Qt.AlignCenter)
        self.L_meter2head.setObjectName("L_meter2head")
        self.L_meter3head = QtWidgets.QLabel(self.G_meterValues)
        self.L_meter3head.setGeometry(QtCore.QRect(660, 80, 131, 41))
        self.L_meter3head.setAlignment(QtCore.Qt.AlignCenter)
        self.L_meter3head.setObjectName("L_meter3head")
        self.L_meter4head = QtWidgets.QLabel(self.G_meterValues)
        self.L_meter4head.setGeometry(QtCore.QRect(890, 80, 131, 41))
        self.L_meter4head.setAlignment(QtCore.Qt.AlignCenter)
        self.L_meter4head.setObjectName("L_meter4head")
        self.B_begin = QtWidgets.QPushButton(self.G_meterValues)
        self.B_begin.setGeometry(QtCore.QRect(30, 190, 131, 41))
        self.B_begin.setObjectName("B_begin")
        self.G_connectionstat = QtWidgets.QGroupBox(self.centralwidget)
        self.G_connectionstat.setGeometry(QtCore.QRect(30, 60, 331, 261))
        self.G_connectionstat.setObjectName("G_connectionstat")
        self.L_comport = QtWidgets.QLabel(self.G_connectionstat)
        self.L_comport.setGeometry(QtCore.QRect(30, 70, 111, 31))
        self.L_comport.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.L_comport.setObjectName("L_comport")
        self.E_comport = QtWidgets.QLineEdit(self.G_connectionstat)
        self.E_comport.setGeometry(QtCore.QRect(140, 71, 113, 31))
        self.E_comport.setObjectName("E_comport")
        self.B_connect = QtWidgets.QPushButton(self.G_connectionstat)
        self.B_connect.setGeometry(QtCore.QRect(20, 190, 131, 41))
        self.B_connect.setObjectName("B_connect")
        self.label = QtWidgets.QLabel(self.G_connectionstat)
        self.label.setGeometry(QtCore.QRect(40, 140, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.G_connectionstat)
        self.label_2.setGeometry(QtCore.QRect(110, 135, 161, 31))
        self.label_2.setStyleSheet("background-color:white;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.G_connectionstat)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 131, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
#----------------------------------------------------------------------------------
        # connecting to the arduino:
        self.B_connect.clicked.connect(self.arduinoConnect)
        self.pushButton.clicked.connect(self.ardclose)
        self.B_begin.clicked.connect(self.bringVals)

#----------------------------------------------------------------------------------
    def arduinoConnect(self):
        try:
            stat = self.E_comport.text()
            self.ard = serial.Serial('com'+stat,9600)
            self.label_2.setText('connection formed')
        except:
            self.label_2.setText('not proper')
            
    def ardclose(self):
        self.ard.close()


    def bringVals(self):
         while True:
            ard.write(b'1')
            var = [0,0,0,0]
            var[0] = ard.readline().decode('utf-8')
            var[1] = ard.readline().decode('utf-8')
            var[2] = ard.readline().decode('utf-8')
            var[3] = ard.readline().decode('utf-8')
            self.L_meter1v.setText(str(var[0]))
            self.L_meter2v.setText(str(var[1]))
            self.L_meter3v.setText(str(var[2]))
            self.L_meter4v.setText(str(var[3]))
            #print(var[0])
            time.sleep(1)
            
    def senderfunc(self):
         worker = Worker(self.bringVals)
         self.threadpool.start(worker)


#----------------------------------------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "arduino Gui interface final"))
        self.G_meterValues.setTitle(_translate("MainWindow", "Meter Values"))
        self.L_meter1head.setText(_translate("MainWindow", "Meter 1"))
        self.L_meter2head.setText(_translate("MainWindow", "Meter 2"))
        self.L_meter3head.setText(_translate("MainWindow", "Meter 3"))
        self.L_meter4head.setText(_translate("MainWindow", "Meter 4"))
        self.B_begin.setText(_translate("MainWindow", "Begin"))
        self.G_connectionstat.setTitle(_translate("MainWindow", "connection status"))
        self.L_comport.setText(_translate("MainWindow", "COM port : "))
        self.B_connect.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "status:"))
        self.pushButton.setText(_translate("MainWindow", "Close Port"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
