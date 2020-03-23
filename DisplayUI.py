from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButtonCam = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonCam.setGeometry(QtCore.QRect(140, 540, 121, 31))
        self.radioButtonCam.setObjectName("radioButtonCam")
        self.radioButtonFile = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonFile.setGeometry(QtCore.QRect(140, 580, 121, 31))
        self.radioButtonFile.setObjectName("radioButtonFile")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setGeometry(QtCore.QRect(350, 560, 121, 41))
        self.Open.setObjectName("Open")
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(550, 560, 111, 41))
        self.Close.setObjectName("Close")
        self.DispalyLabel = QtWidgets.QLabel(self.centralwidget)
        self.DispalyLabel.setGeometry(QtCore.QRect(71, 44, 711, 411))
        self.DispalyLabel.setMouseTracking(False)
        self.DispalyLabel.setText("")
        self.DispalyLabel.setObjectName("DispalyLabel")
        self.AttentivenessLabel = QtWidgets.QLabel(self.centralwidget)
        self.AttentivenessLabel.setObjectName("AttentivenessLabel")
        self.AttentivenessLabel.setGeometry(QtCore.QRect(510, 630, 51, 31))
        self.AttentivenessLabel.setStyleSheet("")
        self.AttentivenessLabel.setScaledContents(False)
        self.AttentivenessLabel.setWordWrap(False)
        self.Attentiveness = QtWidgets.QLCDNumber(self.centralwidget)
        self.Attentiveness.setGeometry(QtCore.QRect(570, 630, 61, 31))
        self.Attentiveness.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);")
        self.Attentiveness.setObjectName("Attentiveness")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 853, 26))
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
        self.radioButtonCam.setText(_translate("MainWindow", "camera"))
        self.radioButtonFile.setText(_translate("MainWindow", "local file"))
        self.Open.setText(_translate("MainWindow", "Open"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.AttentivenessLabel.setText(_translate("MainWindow", "专注率"))
        # self.Attentiveness.setText(_translate("MainWindow", "0.00"))
