# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ui_CamShow(object):
    def setupUi(self, Ui_CamShow):
        Ui_CamShow.setObjectName("Ui_CamShow")
        Ui_CamShow.resize(800, 600)
        self.mainWnd = QtWidgets.QWidget(Ui_CamShow)
        self.mainWnd.setObjectName("mainWnd")
        self.radioButtonCam = QtWidgets.QRadioButton(self.mainWnd)
        self.radioButtonCam.setGeometry(QtCore.QRect(110, 430, 115, 19))
        self.radioButtonCam.setObjectName("radioButtonCam")
        self.radioButtonFile = QtWidgets.QRadioButton(self.mainWnd)
        self.radioButtonFile.setGeometry(QtCore.QRect(110, 480, 115, 19))
        self.radioButtonFile.setObjectName("radioButtonFile")
        self.Open = QtWidgets.QPushButton(self.mainWnd)
        self.Open.setGeometry(QtCore.QRect(380, 430, 93, 28))
        self.Open.setObjectName("Open")
        self.Close = QtWidgets.QPushButton(self.mainWnd)
        self.Close.setGeometry(QtCore.QRect(380, 470, 93, 28))
        self.Close.setObjectName("Close")
        self.frame = QtWidgets.QFrame(self.mainWnd)
        self.frame.setGeometry(QtCore.QRect(70, 50, 661, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.AttentivenessLabel = QtWidgets.QLabel(self.mainWnd)
        self.AttentivenessLabel.setGeometry(QtCore.QRect(510, 440, 51, 31))
        self.AttentivenessLabel.setStyleSheet("")
        self.AttentivenessLabel.setScaledContents(False)
        self.AttentivenessLabel.setWordWrap(False)
        self.AttentivenessLabel.setObjectName("AttentivenessLabel")
        self.Attenttiveness = QtWidgets.QLCDNumber(self.mainWnd)
        self.Attenttiveness.setGeometry(QtCore.QRect(570, 440, 61, 31))
        self.Attenttiveness.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Attenttiveness.setAlignment(QtCore.Qt.AlignCenter)
        self.Attenttiveness.setObjectName("Attenttiveness")
        self.textEdit = QtWidgets.QTextEdit(self.mainWnd)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(640, 410, 104, 75))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        Ui_CamShow.setCentralWidget(self.mainWnd)
        self.menubar = QtWidgets.QMenuBar(Ui_CamShow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Ui_CamShow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_CamShow)
        self.statusbar.setObjectName("statusbar")
        Ui_CamShow.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_CamShow)
        QtCore.QMetaObject.connectSlotsByName(Ui_CamShow)

    def retranslateUi(self, Ui_CamShow):
        _translate = QtCore.QCoreApplication.translate
        Ui_CamShow.setWindowTitle(_translate("Ui_CamShow", "MainWindow"))
        self.radioButtonCam.setText(_translate("Ui_CamShow", "视频"))
        self.radioButtonFile.setText(_translate("Ui_CamShow", "文件"))
        self.Open.setText(_translate("Ui_CamShow", "开始"))
        self.Close.setText(_translate("Ui_CamShow", "关闭"))
        self.AttentivenessLabel.setText(_translate("Ui_CamShow", "专注率"))
        # self.Attenttiveness.setText(_translate("Ui_CamShow", "0.00"))